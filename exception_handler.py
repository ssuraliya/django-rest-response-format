import rest_framework.exceptions as rest_exceptions
from django.core.exceptions import PermissionDenied
from django.core.exceptions import ValidationError as DjangoValidationError
from django.http import Http404
from rest_framework.response import Response
from rest_framework.serializers import as_serializer_error
from rest_framework.views import set_rollback
from rest_framework.settings import api_settings as rest_settings


def custom_exception_handler(exc, context):
    if isinstance(exc, (DjangoValidationError, rest_exceptions.ValidationError)):
        exc = rest_exceptions.ValidationError(as_serializer_error(exc))
        exc.message = "Validation Error"
    elif isinstance(exc, Http404):
        exc = rest_exceptions.NotFound()
    elif isinstance(exc, PermissionDenied):
        exc = rest_exceptions.PermissionDenied()
    elif isinstance(exc, rest_exceptions.APIException):
        exc.detail = {
            rest_settings.NON_FIELD_ERRORS_KEY: [exc.detail]
        }

    if isinstance(exc, rest_exceptions.APIException):
        headers = {}
        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            headers['Retry-After'] = '%d' % exc.wait

        if hasattr(exc, 'message'):
            message = exc.message
        else:
            message = 'Request Failed'
        
        print(exc.detail)
        
        data = {
            'message': message,
            'errors': exc.get_full_details()
        }
        
        set_rollback()
        
        return Response(data, status=exc.status_code, headers=headers)

    return None

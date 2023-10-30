from rest_framework.renderers import JSONRenderer

class CustomJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context['response'].status_code
        response = {
            'message': "Success",
            'data': None,
        }
        
        if str(status_code).startswith('2'):
            if isinstance(data, dict):
                response["message"] = data.get("message", 'Success')
                response["data"] = data.get('data', data)
                if 'pagination' in data:
                    response['pagination'] = data['pagination']
            else:
                response["message"] = 'Success!'
                response["data"] = data 
        else:
            response["data"] = None
            if isinstance(data, dict):
                response["message"] = data.get("message", 'Something went wrong!')
                response["errors"] = data.get('errors', data)
            else:
                response["message"] = 'Success!'
                response["errors"] = data
        
        return super().render(response, accepted_media_type, renderer_context)
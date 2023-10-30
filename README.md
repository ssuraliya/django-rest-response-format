# django-rest-response-format
This repository contains the custom exception handler and response renderer for Django REST framework that helps maintain a standard response format.

The response strucutre using the renderer and exception handle will be:

## REST API Response

1 - Success Response
```javascript
    {
        "message" : "A custom message",
        "data" : {
            "field1": "value",
            "field2": "value"
        }
    }
```

2 - Success Response for list with pagination
```javascript
    {
        "message" : "A custom message",
        "data" : [
            {
                "field1": "value",
                "field2": "value"
            }, 
            {
                "field1": "value",
                "field2": "value"
            }
        ],
        "pagination": {
            "count": 10,
            "next": null,
            "next": null,
        }
    }
```

3 - Error Response for errors not related to request body fields
```javascript
    {
        "message" : "A custom error message",
        "data" : {
            "non_field_errors": [
                {
                    "message": "Something went wrong!",
                    "code": "invalid"
                }
            ]
        }
    }
```

4 - Error Response for errors related to request body fields
```javascript
    {
        "message" : "A custom error message",
        "data" : {
            "email": [
                {
                    "message": "Invalid Email Format",
                    "code": "invalid"
                }
            ],
            "password": [
                {
                    "message": "This field cannot be blank",
                    "code": "blank"
                }
            ]
        }
    }
```

*An extension of [Django Styleguide by Hacksoft's](https://github.com/HackSoftware/Django-Styleguide#approach-2---hacksofts-proposed-way) error handling section.*
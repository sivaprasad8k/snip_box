"""
Middleware module
The module consists Middleware method's that can be used for raising exceptions
------------------------
Coded by: Sivaprasad on 19-06-2023.
© Map My Marketing pvt LTD.
------------------------
"""
import json
import logging
import os
import time
from datetime import datetime
from functools import wraps
from logging.handlers import TimedRotatingFileHandler
from core.functions import generate_response


class ErrorHandlerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)
        status_code = response.status_code
        if status_code == 401:
            # Decode bytes to string
            json_string = response.content.decode('utf-8')
            # Convert JSON string to dictionary
            return generate_response(json.loads(json_string).get('detail'))
        # When loading admin page redirection will happen so the 302 status code will be skipped
        elif status_code != 302 and 200 < status_code < 500:
            return generate_response(status_code)

        elif status_code == 500:
            return generate_response('FAILED')

        elif status_code >= 500:
            return generate_response("SERVER_ERROR")

        else:
            return response

    def process_exception(self, request, exception):
        """Method to catch and handle exceptions in a centralized way before the error is propagated to the view or
        returned to the user."""
        from core.exceptions import manage_exception

        manage_exception(exception)

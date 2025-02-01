from datetime import datetime
from django.http import JsonResponse
from core.enums import Response


def generate_response(status_code, result=None, custom_message=False):
    """ Function to generate the response  dict that needs to be sent back to client. """

    status_code = status_code.value if type(status_code) is Response else status_code

    switcher = {

        404: {"status": "failed", "status_code": status_code,
              "message": "The resource you requested may have been moved, deleted, "
                         "or it might have never existed in the first place."},

        'Authentication credentials were not provided.': {"status": "failed", "status_code": 403,
                                                          "message": "It appears you don't have permission to access this resource."
                                                                     " Please note that access to this content is restricted."},

        405: {"status": "failed", "status_code": status_code, "message": "Method Not Allowed."},

        401: {"status": "failed", "status_code": status_code,
              "message": "It looks like you're not authorized to access this resource. "
                         "Please ensure you have the necessary credentials and try again."},

        'SERVER_ERROR': {"status": "failed", "status_code": status_code,
                         "message": "Unexpected error occurred, please try again after sometime!"},

        'INVALID': {"status": "failed", "status_code": status_code, "message": "Invalid request"},

        'FAILED': {"status": "failed", "status_code": status_code, "message": "Unexpected error occurred"},

        'ERROR': {"status": "failed", "status_code": status_code, "message": "Please try again after some time"},

        Response.ValidationError.value: {"status": "failed", "status_code": status_code, "message": 'Validation Error'},

        Response.DataFound.value: {"status": "success", "status_code": status_code,
                                   "message": "Data retrieved successfully"},

        Response.DataNotFound.value: {"status": "success", "status_code": status_code, "message": "No data found"},

        Response.DataSaved.value: {"status": "success", "status_code": status_code,
                                   "message": "Data saved successfully"},

        Response.DataUpdated.value: {"status": "success", "status_code": status_code,
                                     "message": "Data updated successfully"},

        Response.DataDeleted.value: {"status": "success", "status_code": status_code,
                                     "message": "Data deleted successfully"},
    }
    response = switcher.get(status_code, {"status": "failed", "status_code": status_code, "message": "Invalid request"})

    if result:
        response['result'] = result

    return JsonResponse(response)


def change_date_format(date_str):
    """# Convert string to datetime object to Jan 31 2025 06:37 PM format """
    if date_str:
        date_str = datetime.fromisoformat(date_str).strftime('%b %d %Y %I:%M %p')

    return date_str

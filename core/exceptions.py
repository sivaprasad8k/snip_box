class DataFetchFailedException(Exception):
    pass


def manage_exception(ex):
    """
    @param ex: various type Exceptions raised from APIs
    Method for managing API exceptions
    """
    from core.functions import generate_response
    from core.enums import Response

    if type(ex) == DataFetchFailedException:
        # EXCEPTION WHEN FETCHING DATA FROM THE DATABASE
        return generate_response(Response.DataNotFound)
    else:
        return generate_response("ERROR")

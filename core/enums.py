from enum import Enum


class Response(Enum):
    """ Enum Class for finding response type """
    DataFound = "DATA_FOUND"
    DataNotFound = "DATA_NOT_FOUND"
    DataSaved = "DATA_SAVED"
    ValidationError = "VALIDATION_ERROR"
    DataUpdated = "DATA_UPDATED"
    DataDeleted = "DATA_DELETED"

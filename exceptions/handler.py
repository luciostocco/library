"""
Exceptions handler
"""
from http_response.constants import *


class ApplicationError(Exception):
    STATUS_CODE = HTTP_400_BAD_REQUEST

    def __init__(self, message, payload=None):
        Exception.__init__(self)
        self.message = message
        self.status_code = self.STATUS_CODE
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        rv['status'] = self.status_code
        rv['success'] = False
        return rv


class BadRequestError(ApplicationError):
    STATUS_CODE = HTTP_400_BAD_REQUEST


class UnauthorizedError(ApplicationError):
    STATUS_CODE = HTTP_401_UNAUTHORIZED


class ResourceHasReachedTheLimit(ApplicationError):
    STATUS_CODE = HTTP_402_RESOURCE_HAS_REACHED_THE_LIMIT


class ForbiddenError(ApplicationError):
    STATUS_CODE = HTTP_403_FORBIDDEN


class NotFoundError(ApplicationError):
    STATUS_CODE = HTTP_404_NOT_FOUND

class MethodNotAllowedError(ApplicationError):
    STATUS_CODE = HTTP_405_METHOD_NOT_ALLOWED


class RequestTimeoutError(ApplicationError):
    STATUS_CODE = HTTP_408_REQUEST_TIMEOUT


class ConflictError(ApplicationError):
    STATUS_CODE = HTTP_409_CONFLICT


class ValidationError(ApplicationError):
    STATUS_CODE = HTTP_422_UNPROCESSABLE


class TooManyRequestsError(ApplicationError):
    STATUS_CODE = HTTP_429_TOO_MANY_REQUESTS

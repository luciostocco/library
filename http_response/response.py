"""
Json response handler
"""
from flask import Response
from http_response.constants import HTTP_200_SUCCESS


class JsonResponse(Response):
    """
    Format Json response object
    """

    def __new__(cls, data=None,
                     status=HTTP_200_SUCCESS,
                     success=True,
                     headers=None):

        response_json = {"status": status,
                         "version": "0.1",
                         "success": success}

        if data:
            response_json['data'] = data

        return response_json, status, headers

# -*- coding: utf-8 -*-
"""
app.py: Main API routes handle.
"""
from bootstrap.app import *
from exceptions.handler import BadRequestError, NotFoundError, ValidationError
from http_response.response import JsonResponse
from http_response.constants import HTTP_200_SUCCESS, HTTP_201_CREATED
from helpers.util import email_checker
from helpers.database_seed import DatabaseSeed
from services.book_request_service import BookRequestService
from services.book_service import BookService
from flask import request

# Initialise services
# ==============================
book_request_service = BookRequestService()
book_service = BookService()

# Seed Book Database (If it's empty)
# ==============================
DatabaseSeed().seed_book_table()

# Routes
# ==============================


@app.route('/request', methods=['POST'])
def post_book():

    data = request.get_json()

    if ('email' not in data) or ('title' not in data):
        raise BadRequestError('Schema validation error:: email and title fields are required')

    if not email_checker(data['email']):
        raise BadRequestError('Invalid email')

    if not book_service.does_book_exist(data['title']):
        raise NotFoundError('The requested book does not exist')

    book_request = book_request_service.save(data)

    return JsonResponse(
        data={
            'id': book_request.id,
            'title': book_request.title,
            'email': book_request.mail,
            'timestamp': book_request.timestamp
        },
        status=HTTP_201_CREATED
    )


@app.route('/request/<id>', methods=['GET'])
def get_book_by_id(id):

    response = book_request_service.get_by_id(id)

    if not response:
        raise NotFoundError('Book not found')

    return JsonResponse(
        data=response,
        status=HTTP_200_SUCCESS
    )


@app.route('/request', methods=['GET'])
def list_books():

    response = book_request_service.get_list()

    if not response:
        raise NotFoundError('Book not found')

    return JsonResponse(
        data=response,
        status=HTTP_200_SUCCESS
    )


@app.route('/request/<id>', methods=['DELETE'])
def delete_book(id):

    if not id:
        raise BadRequestError('Id is required')

    book_request_service.delete(id)

    return JsonResponse(status=HTTP_200_SUCCESS)


# Register a default error handler
# ==============================

def default_error_handler(error):
    """
    Default error handler
    """
    return {"status": error.code,
            "message": error.description,
            "success": False}, error.code


app.config['TRAP_HTTP_EXCEPTIONS'] = True
app.register_error_handler(Exception, default_error_handler)

if __name__ == '__main__':
    app.run()

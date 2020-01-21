# -*- coding: utf-8 -*-
from bootstrap.app import *
from services.base_service import BaseService
from models.book_request import BookRequestModel
from sqlalchemy.exc import DBAPIError


class BookRequestService(BaseService):

    def __init__(self):
        super(BookRequestService, self).__init__()

        self.model = BookRequestModel

    def get_by_id(self, id: int):
        """
        Query Book request by id and return its model
        :param id:
        :return: dict / None
        """
        try:
            book_request = self.model.query.filter_by(id=id).first()
        except DBAPIError as err:
            app.logger.log.error(err.orig)
            self.model.session.rollback()
            self.model.session.flush()
            raise err

        if not book_request:
            return None

        return self.format_response(book_request)

    def get_list(self):
        """
        Return book request list
        :return: dict / None
        """
        try:
            book_request_list = self.model.query.all()
        except DBAPIError as err:
            app.logger.log.error(err.orig)
            self.model.session.rollback()
            self.model.session.flush()
            raise err

        if not book_request_list:
            return None

        response_list = []
        for book in book_request_list:
            response_list.append(self.format_response(book))

        return response_list

    def save(self, data: dict):
        """
        Saves a data model in the database and returns its model
        """
        try:
            book_request = self.model(title=data['title'],
                              mail=data['email'])
            db.session.add(book_request)
            db.session.commit()

        except DBAPIError as err:
            app.logger.log.error(err.orig)
            db.session.rollback()
            db.session.flush()
            raise err

        return book_request

    def delete(self, id) -> tuple:
        """
        Deletes a data model in the database
        """

        try:
            self.model.query.filter_by(id=id).delete()
            db.session.commit()
            success = True
        except Exception as err:
            app.logger.log.info(str(err))
            db.session.rollback()
            db.session.flush()
            raise err

        return success

    def format_response(self, book_request: BookRequestModel) -> dict:
        """
        Format the model as an API Response
        """
        return {
            'id': book_request.id,
            'title': book_request.title,
            'email': book_request.mail,
            'timestamp': book_request.timestamp
        }
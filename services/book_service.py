from bootstrap.app import *
from services.base_service import BaseService
from models.book import BookModel
from sqlalchemy.exc import DBAPIError


class BookService(BaseService):

    def __init__(self):
        super(BookService, self).__init__()

        self.model = BookModel

    def get_by_title(self, title: str):
        """
        Query Book by title return its model
        :param id:
        :return: dict / None
        """
        try:
            book = self.model.query.filter_by(title=title).first()
        except DBAPIError as err:
            app.logger.error(err.orig)
            self.model.session.rollback()
            self.model.session.flush()
            raise err

        if not book:
            return None

        return book

    def does_book_exist(self, title: str):
        if self.get_by_title(title):
            return True
        else:
            return False

    def save(self, data: dict):
        """
        Saves a data model in the database and returns its model
        """
        try:
            book = self.model(title=data['title'])
            db.session.add(book)
            db.session.commit()

        except DBAPIError as err:
            app.logger.error(err.orig)
            db.session.rollback()
            db.session.flush()
            raise err

        return book
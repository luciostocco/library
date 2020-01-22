from bootstrap.app import *
from models.book import BookModel
from services.book_service import BookService


class DatabaseSeed:

    def __init__(self):
        self.book_service = BookService()

    def seed_book_table(self):
        """
        Seed Book table
        Only execute if the table is empty
        """
        if not BookModel.query.first():
            app.logger.info('Seeding Book table')
            self.book_service.save({'title': 'Book 1'})
            self.book_service.save({'title': 'Book 2'})
            self.book_service.save({'title': 'Book 3'})
            self.book_service.save({'title': 'Book 4'})
            self.book_service.save({'title': 'Book 5'})

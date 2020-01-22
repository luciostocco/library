from bootstrap.app import *
from sqlalchemy.exc import DBAPIError


class BaseService:
    """
    Base Repository Model
    """

    def __init__(self, *args, **kwargs):
        app.logger.info(f"{self.__class__.__name__}: Initializing new instance. Id: {id(self)}")

        self.create_tables()

    def create_tables(self):
        """
        Create tables if it doesn't exist
        """
        try:
            db.create_all()
            db.session.commit()
        except DBAPIError as err:
            app.logger.error(err)
            raise err

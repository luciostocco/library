import configparser
from flask_sqlalchemy import SQLAlchemy


class DBConnection:
    """
    Db Connection Class
    """

    db_engine = None

    db_host = None
    db_user = None
    db_pass = None
    db_name = None

    @classmethod
    def get_engine(cls, app):
        if not cls.db_engine:
            cls.load_database_config()

            # Initialise database
            app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://{cls.db_user}:{cls.db_pass}@{cls.db_host}/{cls.db_name}"
            app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
            cls.db_engine = SQLAlchemy(app)

        return cls.db_engine

    @classmethod
    def load_database_config(cls):
        """
        Load Database ini file
        """
        config = configparser.ConfigParser()
        config.sections()
        config.read(cls.database_ini_filename_path())
        cls.db_host = config['config']['db_host']
        cls.db_user = config['config']['db_user']
        cls.db_pass = config['config']['db_pass']
        cls.db_name = config['config']['db_name']

    @classmethod
    def database_ini_filename_path(cls):
        return 'config/database.ini'
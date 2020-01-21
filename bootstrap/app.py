# -*- coding: utf-8 -*-
"""
App bootstrap
"""
import os
import socket
import logging
from logging.config import dictConfig
from flask import Flask, jsonify
from exceptions.handler import ApplicationError
from helpers.database_connection import DBConnection


# # Logging Bootstrap
# ==============================
class ContextFilter(logging.Filter):
    hostname = socket.gethostname()

    def filter(self, record):
        record.hostname = ContextFilter.hostname
        return True


logging_configuration = dict(
    version=1,
    disable_existing_loggers=False,
    formatters={
        "default": {"format": "[%(hostname)s %(asctime)s] %(levelname)s in %(message)s"},
    },
    filters={"hostname_filter": {"()": ContextFilter}},
    handlers={
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "filters": ["hostname_filter"],
        }
    },
    root={"handlers": ["console"], "level": os.getenv("LOG_LEVEL", "INFO")},
)

dictConfig(logging_configuration)

logger = logging.getLogger(__name__)

# Flask Bootstrap
# ==============================
app = Flask(__name__)

# Database Bootstrap
# ==============================
db = DBConnection.get_engine(app)


@app.errorhandler(ApplicationError)
def custom_error_handle(error):
    """
    Registering an Custom Error Handler
    :param error: Flask error object
    :return: response
    """
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

from flask import Flask
from os import getenv
import boat_api.utils.logger as logger
import logging
from os import getenv
from flask_sqlalchemy import SQLAlchemy

class FlaskAppFactory:
    """
    Creates a Flask app with config and logger
    """

    def create_app(self, env: str | None) -> Flask:
        app = Flask(__name__)
        app.config["SECRET_KEY"] = getenv("SECRET_KEY")

        log = logging.getLogger(getenv("APP_NAME"))
        logger.configure_logging()

        if env == "development":
            app.config["DEBUG"] = True
            app.config["SQLALCHEMY_DATABASE_URI"] = getenv("SQL_LITE_PATH")
            db = SQLAlchemy(app)
            log.debug("Database path: %s", app.config["SQLALCHEMY_DATABASE_URI"])
        elif env == "production":
            app.config["DEBUG"] = False
        else:
            raise ValueError("Invalid environment name")
        return app

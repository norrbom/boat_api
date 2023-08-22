from gevent import monkey
monkey.patch_all()  # let gevent monkey patch the stdlib
from os import getenv
import os
from boat_api.app import FlaskAppFactory
from boat_api.routes import add_routes
from boat_api.utils.config import load_config

# load env variables from .env file
load_config()

factory = FlaskAppFactory()

# App is running Flask in development mode without WSGI server
if __name__ == "__main__":
    app = factory.create_app("development")
    add_routes(app)
    app.run()

# App is running with a WSGI server
if __name__ != "__main__":
    app = factory.create_app("production")
    add_routes(app)

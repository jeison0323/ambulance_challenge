"""
Init flask module
"""
from handler.error_handler import handle_exceptions
from werkzeug.exceptions import HTTPException
from flask import Flask
from ambulance.routes import ambulance

def create_app():
    """Create the app

    Returns:
        Flask: Flask app
    """
    app = Flask(__name__)

    app.register_blueprint(ambulance)
    app.register_error_handler(HTTPException,handle_exceptions)

    return app

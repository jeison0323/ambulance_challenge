"""
Init flask module
"""
from flask import Flask
from handler.error_handler import errors
from ambulance.routes import ambulance

def create_app():
    """Create the app

    Returns:
        Flask: Flask app
    """
    app = Flask(__name__)

    app.register_blueprint(ambulance)
    app.register_blueprint(errors)
    
    return app

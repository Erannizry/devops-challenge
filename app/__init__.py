from flask import Flask
from dotenv import load_dotenv
from app.routes import blueprints

# Load environment variables from a .env file
load_dotenv()

def create_app(test_config=None):
    """
    Create and configure the Flask application.
    Registers all blueprints found in app.routes.blueprints.
    """
    app = Flask(__name__)

    # Register the routes (blueprints)
    for bp in blueprints:
        app.register_blueprint(bp)

    return app

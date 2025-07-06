from flask import Flask
from dotenv import load_dotenv
from app.routes import blueprints

load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__)

    # Register the routes
    for bp in blueprints:
        app.register_blueprint(bp)

    return app

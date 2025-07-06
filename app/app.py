from flask import Flask
from dotenv import load_dotenv
from routes import blueprints

load_dotenv()

app = Flask(__name__)

for bp in blueprints:
    app.register_blueprint(bp)


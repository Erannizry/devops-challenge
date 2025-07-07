from .secret import secret_bp
from .health import health_bp

# List of all blueprints to be registered with the Flask app
blueprints = [secret_bp, health_bp]

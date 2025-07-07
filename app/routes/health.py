from flask import Blueprint, jsonify

# Blueprint for health check routes
health_bp = Blueprint("health", __name__)

@health_bp.route("/health")
def get_health():
    """
    Health check endpoint.
    Returns a JSON response with project status and metadata.
    """
    return jsonify({
        "container": "https://hub.docker.com/r/eraniz/devops-challenge",
        "project": "https://github.com/Erannizry/devops-challenge",
        "status": "healthy"
    })

from flask import Blueprint, jsonify

health_bp = Blueprint("health", __name__)

@health_bp.route("/health")
def get_health():
    return jsonify({
        "container": "placeholder",
        "project": "https://github.com/Erannizry/devops-challenge",
        "status": "healthy"
    })

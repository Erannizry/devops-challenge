import os
import boto3
from flask import Blueprint, jsonify

# Blueprint for secret-related routes
secret_bp = Blueprint('secret', __name__)

@secret_bp.route("/secret")
def get_secret():
    """
    Retrieve a secret code from DynamoDB using environment variables.
    Returns the secret code as JSON, or an error message if retrieval fails.
    """
    try:
        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table(os.getenv("DYNAMODB_TABLE"))

        response = table.get_item(Key={"codeName": os.getenv("CODE_NAME")})
        return jsonify({"secret_code": response["Item"]})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

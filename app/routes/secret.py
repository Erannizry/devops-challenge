import os
import boto3
from flask import Blueprint, jsonify

secret_bp = Blueprint('secret', __name__)

@secret_bp.route("/secret")
def get_secret():
    try:
        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table(os.getenv("DYNAMODB_TABLE"))

        response = table.get_item(Key={"codeName": os.getenv("CODE_NAME")})
        return jsonify({"secret_code": response["Item"]["secretCode"]})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
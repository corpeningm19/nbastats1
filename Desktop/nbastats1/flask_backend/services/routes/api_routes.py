from flask import Blueprint, jsonify
# from services.models.transaction import Transaction
from services.config import db


api_bp = Blueprint('api', __name__)

@api_bp.route('/data', methods=['GET'])
def get_data():
    data = {'message': 'Hello from the API!'}
    return jsonify(data)

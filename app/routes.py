from flask import request, jsonify
from flask_restful import Api
import uuid
from app.models import in_memory_db
from app.services import calculate_points

def configure_routes(app):
    api = Api(app)

    @app.route('/receipts/process', methods=['POST'])
    def process_receipt():
        data = request.get_json()
        receipt_id = str(uuid.uuid4())
        points = calculate_points(data)
        in_memory_db[receipt_id] = points
        return jsonify({"id": receipt_id})

    @app.route('/receipts/<receipt_id>/points', methods=['GET'])
    def get_points(receipt_id):
        points = in_memory_db.get(receipt_id)
        if points is None:
            return jsonify({"error": "Receipt ID not found"}), 404
        return jsonify({"points": points})

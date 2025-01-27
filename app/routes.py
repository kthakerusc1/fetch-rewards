from flask import request, jsonify
from app.services import calculate_points, get_receipt_points

def configure_routes(app):

    @app.route('/receipts/process', methods=['POST'])
    def process_receipt():
        try:
            data = request.get_json()
            receipt_id = calculate_points(data)
            return jsonify({"id": receipt_id})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route('/receipts/<receipt_id>/points', methods=['GET'])
    def get_points(receipt_id):
        try:
            points = get_receipt_points(receipt_id)
            return jsonify({"points": points})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

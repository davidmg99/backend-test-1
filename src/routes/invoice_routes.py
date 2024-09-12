from flask import Blueprint, request, jsonify
from services import invoice_service

invoice_blueprint = Blueprint('invoice_blueprint', __name__)

@invoice_blueprint.route('/invoice', methods=['GET'])
def get_invoices():
    return jsonify({'message':'aqui estan las facturas'})

@invoice_blueprint.route('/invoice', methods=['POST'])
def create_invoice():
    body = request.get_json()
    invoice = invoice_service.create_new_invoice(body)
    return jsonify({"message": "Invoice created", "invoice_id": invoice.id}), 200
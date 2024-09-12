from flask import Blueprint, request, jsonify
from services import invoice_service

invoice_blueprint = Blueprint('invoice_blueprint', __name__)

@invoice_blueprint.route('/invoice', methods=['GET'])
def get_invoices():
    return jsonify(invoice_service.get_all_invoices())

@invoice_blueprint.route('/invoice', methods=['POST'])
def create_invoice():
    body = request.form
    file = request.files['fileName']
    invoice = invoice_service.create_new_invoice(body, file)
    return jsonify({"message": "Invoice created", "invoice_id": invoice.id}), 200
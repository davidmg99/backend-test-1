from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from services import invoice_service
from schemas.invoice_schema import InvoiceSchema

invoice_blueprint = Blueprint('invoice_blueprint', __name__)

@invoice_blueprint.route('/invoice', methods=['GET'])
def get_invoices():
    return jsonify(invoice_service.get_all_invoices())


@invoice_blueprint.route('/invoice', methods=['POST'])
def create_invoice():
    body = request.form.to_dict()
    if 'fileName' not in request.files:
        return jsonify({"Error": "fileName must be a file"}), 400
    file = request.files['fileName']
    body['fileName'] = file
    schema = InvoiceSchema()

    try:
        schema.load(body)
        invoice = invoice_service.create_new_invoice(body, file)
        return jsonify(schema.dump(invoice)), 200
    except ValidationError as err:
        return jsonify({"Error": err.messages}), 400
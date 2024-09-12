from flask import Blueprint, request, jsonify

invoice_blueprint = Blueprint('invoice_blueprint', __name__)

@invoice_blueprint.route('/invoice', methods=['GET'])
def get_invoices():
    return jsonify({'message':'aqui estan las facturas'})
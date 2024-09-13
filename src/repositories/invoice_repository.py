from models.invoice_model import Invoice
from config import db

def create_invoice(invoice):
    db.session.add(invoice)
    db.session.commit()

def get_all_invoices():
    return Invoice.query.all()
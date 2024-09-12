from repositories import invoice_repository
from models.invoice_model import Invoice
from uuid import uuid4
from datetime import datetime

def create_new_invoice(body):
    new_invoice = Invoice(
        id=str(uuid4()),
        category=body['category'],
        start_period=datetime.fromisoformat(body['startPeriod']),
        end_period=datetime.fromisoformat(body['endPeriod']),
        file_url=f"http://localhost:8002/invoices/{uuid4()}.pdf"
    )
    invoice_repository.create_invoice(new_invoice)
    return new_invoice

def get_all_invoices():
    invoices = invoice_repository.get_all_invoices()
    results = [
        {
            "id": invoice.id,
            "category": invoice.category,
            "startPeriod": invoice.start_period.isoformat(),
            "endPeriod": invoice.end_period.isoformat(),
            "fileUrl": invoice.file_url
        }
        for invoice in invoices
    ]
    return results
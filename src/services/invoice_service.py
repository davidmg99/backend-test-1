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
    return new_invoice
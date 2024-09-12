import os
from flask import current_app as app
from werkzeug.utils import secure_filename
from repositories import invoice_repository
from models.invoice_model import Invoice, CategoryEnum
from uuid import uuid4
from datetime import datetime

def create_new_invoice(body, file):
    if body['category'] not in [cat.value for cat in CategoryEnum]:
        raise ValueError("Invalid category")


    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

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
            "category": invoice.category.value,
            "startPeriod": invoice.start_period.isoformat(),
            "endPeriod": invoice.end_period.isoformat(),
            "fileUrl": invoice.file_url
        }
        for invoice in invoices
    ]
    return results
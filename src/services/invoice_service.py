import os
from flask import current_app as app
from werkzeug.utils import secure_filename
from uuid import uuid4
from datetime import datetime

from repositories import invoice_repository
from models.invoice_model import Invoice, CategoryEnum


def create_new_invoice(body, file):
    if body['category'] not in [cat.value for cat in CategoryEnum]:
        raise ValueError("Invalid category")

    if file and file.filename != "":
        filename = secure_filename(file.filename)
        file_extension = filename.split('.',)[1]
        file_id = str(uuid4())
        new_filename = file_id + "." + file_extension

        file_path = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)
        file.save(file_path)

    new_invoice = Invoice(
        id=file_id,
        category=body['category'],
        start_period=datetime.fromisoformat(body['startPeriod']),
        end_period=datetime.fromisoformat(body['endPeriod']),
        file_url=f"http://localhost:8002/invoices/{file_id}.pdf"
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
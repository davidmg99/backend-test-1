import os
from flask import current_app as app
from werkzeug.utils import secure_filename
from uuid import uuid4
from datetime import datetime

from repositories import invoice_repository
from models.invoice_model import Invoice, CategoryEnum


def create_new_invoice(body, file):
    if file and file.filename != "":
        new_filename = _save_file(file)

    new_invoice = _create_invoice_object(body, new_filename)
    invoice_repository.create_invoice(new_invoice)
    
    return new_invoice


def get_all_invoices():
    invoices = invoice_repository.get_all_invoices()
    return [_format_invoice(invoice) for invoice in invoices]


def _save_file(file):
    filename = secure_filename(file.filename)
    file_extension = filename.rsplit('.', 1)[1]
    file_id = str(uuid4())
    new_filename = f"{file_id}.{file_extension}"

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)
    file.save(file_path)
    
    return new_filename


def _create_invoice_object(body, filename):
    file_id = filename.rsplit('.', 1)[0]
    return Invoice(
        id=file_id,
        category=body['category'],
        start_period=datetime.fromisoformat(body['startPeriod']),
        end_period=datetime.fromisoformat(body['endPeriod']),
        file_url=f"http://localhost:8002/invoices/{file_id}.pdf"
    )


def _format_invoice(invoice):
    return {
        "id": invoice.id,
        "category": invoice.category.value,
        "startPeriod": invoice.start_period.isoformat(),
        "endPeriod": invoice.end_period.isoformat(),
        "fileUrl": invoice.file_url
    }

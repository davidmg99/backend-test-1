from marshmallow import Schema, fields, validates, ValidationError
from datetime import datetime
from models.invoice_model import CategoryEnum

class InvoiceSchema(Schema):
    id = fields.String(required=False)
    category = fields.String(required=True, validate=lambda x: x in [cat.value for cat in CategoryEnum], attribute="category.value")
    start_period = fields.DateTime(format='%Y-%m-%dT%H:%M:%S', required=True, data_key='startPeriod')
    end_period = fields.DateTime(format='%Y-%m-%dT%H:%M:%S', required=True, data_key='endPeriod')
    file_url = fields.String(data_key='fileUrl')
    file_name = fields.Raw(required=True, data_key='fileName')

    @validates("file_name")
    def validate_file(self, file):
        if not file or not hasattr(file, 'filename'):
            raise ValidationError("A valid file is required.")

from config import db
from enum import Enum

class CategoryEnum(Enum):
    b2b = 'b2b'
    b2c = 'b2c'
    operations = 'operations'

class Invoice(db.Model):
    __tablename__ = 'invoices'
    
    id = db.Column(db.String, primary_key=True)
    category = db.Column(db.Enum(CategoryEnum), nullable=False)
    start_period = db.Column(db.DateTime, nullable=False)
    end_period = db.Column(db.DateTime, nullable=False)
    file_url = db.Column(db.String(255), nullable=False)

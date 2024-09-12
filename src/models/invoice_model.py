from config import db

# Definir el modelo para la tabla 'invoices'
class Invoice(db.Model):
    __tablename__ = 'invoices'  # Nombre de la tabla en la base de datos
    
    id = db.Column(db.String, primary_key=True)
    category = db.Column(db.String(50), nullable=False)
    start_period = db.Column(db.DateTime, nullable=False)
    end_period = db.Column(db.DateTime, nullable=False)
    file_url = db.Column(db.String(255), nullable=False)

import os
from flask_sqlalchemy import SQLAlchemy

# Inicializamos la instancia de la base de datos
db = SQLAlchemy()

# Clase base para configuraciones generales
class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = '/app/invoices'

# Configuración específica para desarrollo
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@db:5432/postgres'
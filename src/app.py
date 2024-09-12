from flask import Flask
from config import db
from routes.invoice_routes import invoice_blueprint

app = Flask(__name__)

# Base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db:5432/postgres'
db.init_app(app)

# Upload folder with the invoices
app.config['UPLOAD_FOLDER'] = '/app/uploads'

# Blueprints
app.register_blueprint(invoice_blueprint)

def page_not_found(error):
    return "<h1>Page not found</h1>"

if __name__ == '__main__':

    app.register_error_handler(404, page_not_found)
    app.run(host='0.0.0.0', port=8002, debug=True)

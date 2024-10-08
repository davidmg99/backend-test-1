from flask import Flask
from config import db, DevelopmentConfig 
from routes.invoice_routes import invoice_blueprint

app = Flask(__name__)

app.config.from_object(DevelopmentConfig)

db.init_app(app)

app.register_blueprint(invoice_blueprint)

def page_not_found(error):
    return "<h1>Page not found</h1>"

if __name__ == '__main__':
    app.register_error_handler(404, page_not_found)
    app.run(host='0.0.0.0', port=8002)

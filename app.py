from flask import Flask
from flask_migrate import Migrate
from models.models import db
from routes.auth_routes import auth_bp
from routes.main_routes import main_bp
from routes.member_routes import member_bp
from routes.transaction_routes import transaction_bp
import os

app = Flask(__name__)

# Konfigurasi
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///koperasi.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inisialisasi Database
db.init_app(app)
migrate = Migrate(app, db)

# Blueprint (urutan penting!)
app.register_blueprint(main_bp)         # Halaman utama (landing)
app.register_blueprint(auth_bp, url_prefix="/auth")   # Login/Register
app.register_blueprint(member_bp, url_prefix="/anggota")
app.register_blueprint(transaction_bp, url_prefix="/transaksi")

if __name__ == '__main__':
    app.run(debug=True)

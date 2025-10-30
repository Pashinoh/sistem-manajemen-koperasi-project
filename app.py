from flask import Flask
from flask_migrate import Migrate
from models.models import db
from routes.auth_routes import auth_bp
from routes.main_routes import main_bp
import os

app = Flask(__name__)

# Konfigurasi
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///koperasi.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inisialisasi Database
db.init_app(app)
migrate = Migrate(app, db)

# Blueprint
app.register_blueprint(auth_bp)
app.register_blueprint(main_bp)

@app.route('/')
def index():
    return "Selamat datang di Sistem Manajemen Koperasi!"

if __name__ == '__main__':
    app.run(debug=True)

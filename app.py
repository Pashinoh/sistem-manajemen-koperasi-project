from flask import Flask, render_template
from flask_migrate import Migrate
from flask_login import LoginManager
from models import db
from models.user_model import User
from routes.auth_routes import auth_bp
from routes.transaction_routes import transaction_bp
from routes.main_routes import main  # pastikan nama sesuai file
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'  # mengarah ke endpoint blueprint auth

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# register blueprint
app.register_blueprint(auth_bp)
app.register_blueprint(transaction_bp)  # sudah ada di repo
app.register_blueprint(main)

@app.route('/')
def landing():
    return render_template('landing.html')

if __name__ == '__main__':
    app.run(debug=True)

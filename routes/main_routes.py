# routes/main_routes.py
from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/dashboard')
@login_required
def dashboard():
    # current_user berasal dari flask-login
    if getattr(current_user, 'role', 'user') == 'admin':
        return render_template('dashboard_admin.html', user=current_user)
    return render_template('dashboard_user.html', user=current_user)

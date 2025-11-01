# routes/auth_routes.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from models import db
from models.user_model import User

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = (request.form.get('username') or "").strip()
        password = request.form.get('password') or ""

        if not username or not password:
            flash('Username dan password harus diisi.', 'warning')
            return render_template('login.html')

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            # redirect ke dashboard pusat
            return redirect(url_for('main.dashboard'))
        else:
            flash('Username atau password salah.', 'danger')

    return render_template('login.html')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = (request.form.get('username') or "").strip()
        email = (request.form.get('email') or "").strip()
        password = request.form.get('password') or ""

        # Validasi sederhana
        if not username or not email or not password:
            flash('Semua field harus diisi.', 'warning')
            return render_template('register.html')

        if User.query.filter_by(username=username).first():
            flash('Username sudah digunakan.', 'warning')
            return redirect(url_for('auth.register'))

        if User.query.filter_by(email=email).first():
            flash('Email sudah digunakan.', 'warning')
            return redirect(url_for('auth.register'))

        new_user = User(username=username, email=email, role='user')  # default user
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registrasi berhasil. Silakan login.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Anda telah logout.', 'info')
    return redirect(url_for('auth.login'))

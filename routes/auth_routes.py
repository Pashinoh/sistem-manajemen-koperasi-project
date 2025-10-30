from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['username'] = user.username
            session['role'] = user.role
            flash('Login berhasil', 'success')
            return redirect(url_for('main.dashboard'))

        flash('Username atau password salah', 'danger')
    return render_template('login.html')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Cek apakah username sudah ada
        if User.query.filter_by(username=username).first():
            flash('Username sudah terdaftar', 'warning')
            return redirect(url_for('auth.register'))

        # Hash password
        hashed = generate_password_hash(password)

        # Default role adalah 'anggota'
        user = User(username=username, password=hashed, role='anggota')
        db.session.add(user)
        db.session.commit()

        flash('Registrasi berhasil. Silakan login.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')


@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('Berhasil logout', 'info')
    return redirect(url_for('auth.login'))

from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.models import db, User

member_bp = Blueprint('member', __name__)

@member_bp.route('/anggota')
def anggota_list():
    if 'user_id' not in session:
        flash('Silakan login dulu', 'warning')
        return redirect(url_for('auth.login'))
    
    # Hanya admin yang bisa lihat semua anggota
    if session.get('role') != 'admin':
        flash('Akses ditolak, hanya admin yang dapat melihat daftar anggota.', 'danger')
        return redirect(url_for('main.dashboard'))

    anggota = User.query.all()
    return render_template('anggota.html', anggota=anggota)

@member_bp.route('/hapus_anggota/<int:id>', methods=['POST'])
def hapus_anggota(id):
    if session.get('role') != 'admin':
        flash('Akses ditolak', 'danger')
        return redirect(url_for('main.dashboard'))
    
    user = User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
        flash('Anggota berhasil dihapus', 'success')
    return redirect(url_for('member.anggota_list'))

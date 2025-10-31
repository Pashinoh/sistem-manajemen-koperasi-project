from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.transaction import Transaction
from models.models import db

transaction_bp = Blueprint('transaction', __name__)

@transaction_bp.route('/transaksi', methods=['GET', 'POST'])
def transaksi():
    if 'user_id' not in session:
        flash('Silakan login dulu', 'warning')
        return redirect(url_for('auth.login'))
    
    if request.method == 'POST':
        tipe = request.form.get('type')
        jumlah = float(request.form.get('amount'))

        if jumlah <= 0:
            flash('Jumlah harus lebih besar dari 0', 'danger')
            return redirect(url_for('transaction.transaksi'))

        transaksi = Transaction(user_id=session['user_id'], type=tipe, amount=jumlah)
        db.session.add(transaksi)
        db.session.commit()
        flash('Transaksi berhasil disimpan!', 'success')
        return redirect(url_for('transaction.transaksi'))

    semua = Transaction.query.filter_by(user_id=session['user_id']).all()
    return render_template('transaksi.html', transaksi=semua)

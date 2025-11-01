from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models.transaction_model import Transaction
from models import db

transaction_bp = Blueprint('transaction', __name__)

@transaction_bp.route('/transactions')
@login_required
def user_transactions():
    transactions = Transaction.query.filter_by(user_id=current_user.id).all()
    return render_template('transactions.html', transactions=transactions)


@transaction_bp.route('/transactions/add', methods=['GET', 'POST'])
@login_required
def add_transaction():
    if request.method == 'POST':
        t_type = request.form['type']
        amount = float(request.form['amount'])

        new_trx = Transaction(user_id=current_user.id, type=t_type, amount=amount)
        db.session.add(new_trx)
        db.session.commit()
        flash('Transaksi berhasil ditambahkan.', 'success')
        return redirect(url_for('transaction.user_transactions'))

    return render_template('add_transaction.html')


# Admin page
@transaction_bp.route('/admin/transactions')
@login_required
def admin_transactions():
    if current_user.role != 'admin':
        flash('Akses ditolak.', 'danger')
        return redirect(url_for('transaction.user_transactions'))

    transactions = Transaction.query.all()
    return render_template('admin_transactions.html', transactions=transactions)


@transaction_bp.route('/admin/transactions/update/<int:id>', methods=['POST'])
@login_required
def update_transaction(id):
    if current_user.role != 'admin':
        flash('Akses ditolak.', 'danger')
        return redirect(url_for('transaction.user_transactions'))

    trx = Transaction.query.get(id)
    trx.status = request.form['status']
    db.session.commit()
    flash('Status transaksi diperbarui.', 'success')
    return redirect(url_for('transaction.admin_transactions'))

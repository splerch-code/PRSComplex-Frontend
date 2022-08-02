from datetime import datetime
from rps import app
from flask import render_template, redirect, url_for, flash, request
from rps.forms import *
from rps.models import *
from flask_login import login_user, logout_user, login_required


def flash_form_errors(form):
    """
    Creates bootstrap errors messages for invalid form fields
    :param form:
    :return:
    """
    for err_msg in form.errors.values():
        flash(list(err_msg)[0], category='danger')


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def index():
    # login form
    login_form = LoginForm()
    if login_form.submit.data:
        if login_form.validate_on_submit():
            attempted_user = User.query.filter_by(username=login_form.username.data).first()
            if attempted_user and attempted_user.check_password_correction(login_form.password.data):
                login_user(attempted_user)
                print('user signed in')
            else:
                flash('Invalid credentials', category='danger')
        if login_form.errors:
            flash_form_errors(login_form)

    # new account form
    new_account_form = NewAccountForm()
    if new_account_form.create_account.data:
        if new_account_form.validate_on_submit():
            new_user = User(
                username=new_account_form.username.data,
                email=new_account_form.email.data,
                password=new_account_form.password.data
            )
            db.session.add(new_user)
            create_attempt = LoginAttempt(
                user_id=new_user.id,
                attempt_dt=datetime.now(),
                result='Created'
            )
            db.session.add(create_attempt)
            db.session.commit()
            login_user(new_user)
            flash('Account successfully created!', category='success')
            return redirect(request.url)
        if new_account_form.errors:
            flash_form_errors(new_account_form)

    return render_template('base.html', login_form=login_form, new_account_form=new_account_form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash("You've successfully logged out", category='info')
    return redirect(url_for('index'))

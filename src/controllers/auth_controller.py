from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required
from route.auth import auth
from src.models.User import User
from src.forms.login_form import LoginForm
from src.forms.register_form import RegistrationForm
from src.app import db

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('home.index'))
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('home.index'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    # if submit -> get data from form -> save into DB -> redirect auth/login
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        flash('You can now login.')
        return redirect(url_for('auth.login'))
    # else render: register.html
    return render_template('auth/register.html', form=form)
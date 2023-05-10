from flask import current_app, Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

auth = Blueprint('auth', __name__)

# limiter = Limiter(current_app, key_func=get_remote_address)
limiter = Limiter(get_remote_address, app=current_app, default_limits=["200 per day", "50 per hour"])
tries = 4

@auth.route('/login', methods=['GET', 'POST'])
@limiter.limit("3 per minute")
def login():
    global tries
    requester_ip = request.remote_addr
    header = "PIN"
    # showMe = current_app.config['home'].rooms[2].blinds[0].room


    if User.query.count() < 1:

        newUser = User(pin=generate_password_hash("478026", method='sha256'))
        flash(User.query.count())
        db.session.add(newUser)
        db.session.commit()

    if request.method == 'POST':
        pin = request.form.get('pinField')
        users = User.query.all()
        for user in users:
            if check_password_hash(user.pin, pin):
                login_user(user, remember=False)
                return redirect(url_for('views.home'))

       
    return render_template("login.html", user=current_user, tries=tries, header=header)




@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(username=username).first()
        if user:
            flash('username already exists.', category='error')
        elif len(username) < 4:
            flash('username must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(username=username, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)
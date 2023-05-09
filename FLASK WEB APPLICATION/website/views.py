from flask import flash, current_app, Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():

    house = current_app.config['home']

    return render_template("home.html", user=current_user, house=house)

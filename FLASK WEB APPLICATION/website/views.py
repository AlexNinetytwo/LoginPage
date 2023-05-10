from flask import flash, current_app, Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def sentToHome():
    return redirect(url_for('views.home'))

@views.route('/Home', methods=['GET', 'POST'])
@login_required
def home():

    header = "HOME"
    house = current_app.config['home']
    return render_template("home.html", house=house, header=header)

@views.route('/Wohnzimmer', methods=['GET', 'POST'])
@login_required
def livingRoom():

    header = "WOHNZIMMER"
    house = current_app.config['home']
    previousPage = "/Home"
    return render_template("room.html", house=house, header=header, previousPage=previousPage)

@views.route('/Schlafzimmer', methods=['GET', 'POST'])
@login_required
def bedRoom():

    header = "SCHLAFZIMMER"
    house = current_app.config['home']
    previousPage = "/Home"
    return render_template("room.html", house=house, header=header, previousPage=previousPage)

@views.route('/Kinderzimmer', methods=['GET', 'POST'])
@login_required
def nurery():

    header = "KINDERZIMMER"
    house = current_app.config['home']
    previousPage = "/Home"
    return render_template("room.html", house=house, header=header, previousPage=previousPage)

@views.route('/Alle', methods=['GET', 'POST'])
@login_required
def all():

    header = "ALLE"
    house = current_app.config['home']
    previousPage = "/Home"
    return render_template("room.html", house=house, header=header, previousPage=previousPage)

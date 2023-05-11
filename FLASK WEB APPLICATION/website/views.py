from flask import flash, current_app, Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

def getTemp():
    return "21°C"

@views.route('/', methods=['GET', 'POST'])
def sentToHome():
    return redirect(url_for('views.home'))

@views.route('/Home', methods=['GET', 'POST'])
@login_required
def home():
    header = "HOME"
    house = current_app.config['home'] 
    return render_template("menu.html",
                           house=house,
                           header=header,
                           celsius = getTemp(),
                           floor=False)

@views.route('/Home/Erdgeschoss', methods=['GET', 'POST'])
@login_required
def groundFloor():
    header = "ERDGESCHOSS"
    house = current_app.config['home']
    previousPage = "/Home"
    return render_template("menu.html",
                           house=house,
                           header=header,
                           celsius=getTemp(),
                           previousPage=previousPage,
                           isFloor=True,
                           floor=house.floors[0])

@views.route('/Home/1.OG', methods=['GET', 'POST'])
@login_required
def firstFloor():
    header = "1.OG"
    house = current_app.config['home']
    previousPage = "/Home"
    return render_template("menu.html",
                           house=house,
                           header=header,
                           celsius=getTemp(),
                           previousPage=previousPage,
                           isFloor=True,
                           floor=house.floors[1])

@views.route('/Home/Wohnzimmer', methods=['GET', 'POST'])
@login_required
def livingRoom():
    header = "WOHNZIMMER"
    house = current_app.config['home']
    previousPage = "/Home"
    return render_template("room.html",
                           house=house,
                           header=header,
                           celsius = getTemp(),
                           previousPage=previousPage)

@views.route('/Home/Esszimmer', methods=['GET', 'POST'])
@login_required
def bedRoom():
    header = "ESSZIMMER"
    house = current_app.config['home']
    previousPage = "/Home"
    return render_template("room.html",
                           house=house,
                           header=header,
                           celsius=getTemp(),
                           previousPage=previousPage)

@views.route('/Home/Kinderzimmer', methods=['GET', 'POST'])
@login_required
def nurery():
    header = "KINDERZIMMER"
    house = current_app.config['home']
    previousPage = "/Home"
    return render_template("room.html",
                            house=house,
                            header=header,
                            celsius=getTemp(),
                            previousPage=previousPage)

@views.route('/Home/Alle', methods=['GET', 'POST'])
@login_required
def all():
    header = "ALLE"
    house = current_app.config['home']
    previousPage = "/Home"
    return render_template("room.html",
                            house=house,
                            header=header,
                            celsius=getTemp(),
                            previousPage=previousPage)

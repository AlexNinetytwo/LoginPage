from flask import flash, current_app, Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from .models import *

views = Blueprint('views', __name__)

def getTemp():
    return "21°C"

@views.route('/', methods=['GET', 'POST'])
def sentToHome():
    return redirect(url_for('views.home'))



@views.route('/Home', methods=['GET', 'POST'])
@login_required
def home():
    house = House.query.filter_by(id=1)
    envs = Floor.query.all()
    return render_template('home.html',envs=envs, house=house, celsius=getTemp(), header='HOME')

@views.route('/Home/Erdgeschoss', methods=['GET', 'POST'])
@login_required
def groundFloor():
    template = "floor.html"
    name = "Erdgeschoss"
    floor_id = Floor.query.filter_by(name="Erdgeschoss").first().id
    rooms = Room.query.filter_by(floor_id=floor_id)
    header = name.upper()
    previousPage = "/Home"
    
    return render_template(template,
                            name=name,
                            rooms=rooms,
                            celsius=getTemp(),
                            header=header,
                            previousPage=previousPage)


@views.route('/Home/1.OG', methods=['GET', 'POST'])
@login_required
def firstFloor():
    template = "floor.html"
    name = "1.OG"
    floor_id = Floor.query.filter_by(name="1.OG").first().id
    rooms = Room.query.filter_by(floor_id=floor_id)
    header = name
    previousPage = "/Home"
    
    return render_template(template,
                            name=name,
                            rooms=rooms,
                            celsius=getTemp(),
                            header=header,
                            previousPage=previousPage)


@views.route('/Home/Erdgeschoss/Wohnzimmer', methods=['GET', 'POST'])
@login_required
def livingroom():
    template = "room.html"
    name = "Wohnzimmer"
    header = name.upper()
    previousPage = "/Home/Erdgeschoss"
    room_id = Room.query.filter_by(name=name).first().id
    modules = Blind.query.filter_by(id=room_id)
    
    return render_template(template,
                            modules=modules,
                            name=name,
                            celsius=getTemp(),
                            header=header,
                            previousPage=previousPage)




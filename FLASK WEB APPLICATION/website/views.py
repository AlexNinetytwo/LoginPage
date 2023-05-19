from flask import request, jsonify, flash, current_app, Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from .models import *

views = Blueprint('views', __name__)

def getTemp():
    return "21°C"

@views.route('/', methods=['GET', 'POST'])
def sentToHome():
    return redirect(url_for('views.home'))

@views.route("/autoOnOff", methods=["POST"])
def autoOnOff():
    port = int(request.form.get("port"))
    module = Light.query.filter_by(port=port).first()
    try:
        module.auto = False if module.auto == True else True
    except:
        module = Blind.query.filter_by(port=port).first()
        module.auto = False if module.auto == True else True
    finally:
        db.session.commit()
    
    return jsonify(result="success")

@views.route("/getTimeEntries/<int:id>", methods=["GET"])
def getTimeEntries(id):
    timeEntries = BlindsActionTimes.query.filter_by(blind_id=id)
    return jsonify(data=[item.serialize() for item in timeEntries])

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

@views.route('/Home/Erdgeschoss/Flur', methods=['GET', 'POST'])
@login_required
def hallway():
    template = "room.html"
    name = "Flur"
    header = name.upper()
    previousPage = "/Home/Erdgeschoss"
    id = Room.query.filter_by(name=name).first().id
    blinds = Blind.query.filter_by(room_id=id)
    lights = Light.query.filter_by(room_id=id)
    modules = {'blinds':blinds, 'lights':lights}
    
    return render_template(template,
                            modules=modules,
                            name=name,
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
    id = Room.query.filter_by(name=name).first().id
    blinds = Blind.query.filter_by(room_id=id)
    lights = Light.query.filter_by(room_id=id)
    modules = {'lights':lights, 'blinds':blinds}
    
    return render_template(template,
                            modules=modules,
                            name=name,
                            celsius=getTemp(),
                            header=header,
                            previousPage=previousPage)

@views.route('/Home/Erdgeschoss/Esszimmer', methods=['GET', 'POST'])
@login_required
def diningroom():
    template = "room.html"
    name = "Esszimmer"
    header = name.upper()
    previousPage = "/Home/Erdgeschoss"
    id = Room.query.filter_by(name=name).first().id
    blinds = Blind.query.filter_by(room_id=id)
    lights = Light.query.filter_by(room_id=id)
    modules = {'lights':lights, 'blinds':blinds}
    
    return render_template(template,
                            modules=modules,
                            name=name,
                            celsius=getTemp(),
                            header=header,
                            previousPage=previousPage)

@views.route('/Home/Erdgeschoss/Küche', methods=['GET', 'POST'])
@login_required
def kitchen():
    template = "room.html"
    name = "Küche"
    header = name.upper()
    previousPage = "/Home/Erdgeschoss"
    id = Room.query.filter_by(name=name).first().id
    blinds = Blind.query.filter_by(room_id=id)
    lights = Light.query.filter_by(room_id=id)
    modules = {'blinds':blinds, 'lights':lights}
    
    return render_template(template,
                            modules=modules,
                            name=name,
                            celsius=getTemp(),
                            header=header,
                            previousPage=previousPage)




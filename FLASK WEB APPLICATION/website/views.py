from flask import request, jsonify, flash, current_app, Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.exc import IntegrityError
from datetime import time as dt_time
from .models import *


views = Blueprint('views', __name__)

def getTemp():
    return "21°C"


@views.route("/updateButtonStates/<int:port>", methods=["POST"])
def updateButtonStates(port):
    newState = request.form.get("newState")
    current_app.config["DRIVE_BUTTON_STATES"][port] = newState
    return "success"

@views.route("/getButtonStates", methods=['GET'])
def getButtonStates():
    return jsonify(data=current_app.config["DRIVE_BUTTON_STATES"])

@views.route('/', methods=['GET', 'POST'])
def sentToHome():
    return redirect(url_for('views.home'))


@views.route("/autoOnOff/<int:id>", methods=["POST"])
def autoOnOff(id):
    id = int(id)
    target = int(request.form.get("target"))

    if target == ""
    
    return jsonify(result="success")



@views.route("/getTimeEntries/<int:id>", methods=["GET"])
def getTimeEntries(id):
    timeEntries = BlindsActionTimes.query.filter_by(blind_id=id)
    return jsonify(data=[item.serialize() for item in timeEntries])

@views.route("/saveNewAction/<int:id>", methods=["POST"])
def saveNewAction(id):
    time = request.form.get("time")
    action = int(request.form.get("action"))

    timeParts = time.split(":")
    hours = int(timeParts[0])
    minutes = int(timeParts[1])
    newTime = dt_time(hours, minutes)

    for blindAction in BlindsActionTimes.query.all():
        if blindAction.time_value == newTime and blindAction.blind_id == id:
            blindAction.time_value = newTime
            blindAction.closedInPercent = action
            db.session.commit()
            return "overwritten"
        
    newAction = BlindsActionTimes(blind_id=id, time_value=newTime, closedInPercent=action)

    db.session.add(newAction)
    db.session.commit()

    return "success"

@views.route("/deleteAction/<int:id>", methods=["POST"])
def deleteAction(id):
    action = BlindsActionTimes.query.get(id)
    db.session.delete(action)
    db.session.commit()

    return "deleted"

@views.route('/Home', methods=['GET', 'POST'])
@login_required
def home():
    house = House.query.filter_by(id=1)
    envs = Floor.query.all()
    return render_template('home.html',envs=envs, house=house, celsius=getTemp(), header='HOME')

@views.route('/Home/Alle', methods=['GET', 'POST'])
@login_required
def all():
    template = "room.html"
    name = "Alle"
    header = name.upper()
    previousPage = "/Home"

    return render_template(template,
                            celsius=getTemp(),
                            header=header,
                            previousPage=previousPage)

@views.route('/Home/Erdgeschoss', methods=['GET', 'POST'])
@login_required
def groundFloor():
    template = "floor.html"
    name = "Erdgeschoss"
    floor = Floor.query.filter_by(name="Erdgeschoss").first()
    header = name.upper()
    previousPage = "/Home"
    
    return render_template(template,
                            floor=floor,
                            celsius=getTemp(),
                            header=header,
                            previousPage=previousPage)

@views.route('/Home/1.OG', methods=['GET', 'POST'])
@login_required
def firstFloor():
    template = "floor.html"
    name = "1.OG"
    floor = Floor.query.filter_by(name="1.OG").first()
    header = name
    previousPage = "/Home"
    
    return render_template(template,
                            floor=floor,
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
    room = Room.query.filter_by(name=name).first()
    
    return render_template(template,
                            room=room,
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
    room = Room.query.filter_by(name=name).first()
    
    return render_template(template,
                            room=room,
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
    room = Room.query.filter_by(name=name).first()
    
    return render_template(template,
                            room=room,    
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
    room = Room.query.filter_by(name=name).first()
    
    return render_template(template,
                            room=room,
                            celsius=getTemp(),
                            header=header,
                            previousPage=previousPage)

@views.route('/Home/1.OG/Büro1', methods=['GET', 'POST'])
@login_required
def office1():
    template = "room.html"
    name = "Büro1"
    header = name.upper()
    previousPage = "/Home/1.OG"
    room = Room.query.filter_by(name=name).first()
    
    return render_template(template,
                            room=room,
                            celsius=getTemp(),
                            header=header,
                            previousPage=previousPage)

@views.route('/Home/1.OG/Büro2', methods=['GET', 'POST'])
@login_required
def office2():
    template = "room.html"
    name = "Büro2"
    header = name.upper()
    previousPage = "/Home/1.OG"
    room = Room.query.filter_by(name=name).first()
    
    return render_template(template,
                            room=room,
                            celsius=getTemp(),
                            header=header,
                            previousPage=previousPage)

@views.route('/Home/1.OG/Herrenzimmer', methods=['GET', 'POST'])
@login_required
def menroom():
    template = "room.html"
    name = "Herrenzimmer"
    header = name.upper()
    previousPage = "/Home/1.OG"
    room = Room.query.filter_by(name=name).first()
    
    return render_template(template,
                            room=room,
                            celsius=getTemp(),
                            header=header,
                            previousPage=previousPage)




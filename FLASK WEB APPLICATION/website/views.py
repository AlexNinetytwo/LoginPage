from flask import request, jsonify, flash, current_app, Blueprint, render_template, redirect, url_for
from flask_login import login_required
from datetime import time as dt_time
from .models import *
from . import temperatureAPI

views = Blueprint('views', __name__)

@views.route("/updateCurrentActions", methods=["POST"])
def updateCurrentActions(buttons):
    port = 1
    if port != -1:
        light = Light.query.filter_by(port=port).first()
        light.turnOff()
    else:
        for light in Light.query.all():
            light.turnOff()
    return "success"

@views.route("/turnLightOff/<int:port>", methods=["POST"])
def turnLightOff(port):
    if port != -1:
        light = Light.query.filter_by(port=port).first()
        light.turnOff()
    else:
        for light in Light.query.all():
            light.turnOff()
    return "success"

@views.route("/turnLightOn/<int:id>", methods=["POST"])
def turnLightOn(port):
    if port != -1:
        light = Light.query.filter_by(port=port).first()
        light.query.get(id).turnOn()
    else:
        for light in Light.query.all():
            light.turnOn()
    return "success"

@views.route("/currentTemperature", methods=['GET'])
def getCurrentTemperature():
    # return temperatureAPI.currentTemperature()
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


@views.route("/switchAutomatic/<int:port>", methods=["POST"])
def switchAutomatic(port):
    port = int(port)
    module = House.getModuleByPort(port)
    module.switchAutomatic()
    
    return jsonify(result="success")

@views.route("/switchEnvAutomatic/<int:env_id>", methods=["POST"])
def switchEnvAutomatic(env_id):
    env = request.form.get("enviroment")
    moduleType = request.form.get("moduleType")

    try:


        if env == "HomeSystem":
            House.query.get(env_id).switchAutomatic(moduleType) 

        elif env == "Erdgeschoss" or env == "1.OG":
            Floor.query.get(env_id).switchAutomatic(moduleType)
        
        else:
            Room.query.get(env_id).switchAutomatic(moduleType)

    except Exception as e:
        print(e)

    return jsonify(result="success")




@views.route("/getTimeEntries/<int:id>", methods=["GET"])
def getTimeEntries(id):
    timeEntries = BlindsActionTimes.query.filter_by(blind_id=id)
    return jsonify(data=[item.serialize() for item in timeEntries])

@views.route("/saveNewAction/<int:id>", methods=["POST"])
def saveNewAction(id):
    time = request.form.get("time")
    action = int(request.form.get("action"))
    blind = Blind.query.get(id)

    timeParts = time.split(":")
    hours = int(timeParts[0])
    minutes = int(timeParts[1])
    newTime = dt_time(hours, minutes)

    blind.addActionTime(newTime, action)
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
    house = House.query.get(1)
    return render_template('home.html', house=house, celsius=getCurrentTemperature(), header='HOME')

@views.route('/Home/Alle', methods=['GET', 'POST'])
@login_required
def all():
    template = "room.html"
    name = "Alle"
    header = name.upper()
    previousPage = "/Home"
    room = House.query.get(1)


    return render_template(template,
                            celsius=getCurrentTemperature(),
                            room=room,
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
    allLinkFiller = name + "/"
    
    return render_template(template,
                            allLinkFiller=allLinkFiller,
                            floor=floor,
                            celsius=getCurrentTemperature(),
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
    allLinkFiller = name + "/"
    
    return render_template(template,
                            floor=floor,
                            allLinkFiller=allLinkFiller,
                            celsius=getCurrentTemperature(),
                            header=header,
                            previousPage=previousPage)

@views.route('/Home/Erdgeschoss/Alle', methods=['GET', 'POST'])
@login_required
def groundFloorAll():
    template = "room.html"
    header = "ALLE ERDGESCHOSS"
    previousPage = "/Home/Erdgeschoss"
    room = Floor.query.filter_by(name="Erdgeschoss").first()
    
    return render_template(template,
                            room=room,
                            celsius=getCurrentTemperature(),
                            header=header,
                            previousPage=previousPage)

@views.route('/Home/1.OG/Alle', methods=['GET', 'POST'])
@login_required
def firstFloorAll():
    template = "room.html"
    header = "ALLE 1.OG"
    previousPage = "/Home/1.OG"
    room = Floor.query.filter_by(name="1.OG").first()
    
    return render_template(template,
                            room=room,
                            celsius=getCurrentTemperature(),
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
                            celsius=getCurrentTemperature(),
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
                            celsius=getCurrentTemperature(),
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
                            celsius=getCurrentTemperature(),
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
                            celsius=getCurrentTemperature(),
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
                            celsius=getCurrentTemperature(),
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
                            celsius=getCurrentTemperature(),
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
                            celsius=getCurrentTemperature(),
                            header=header,
                            previousPage=previousPage)




from . import db
from .models import Blind, BlindsActionTimes, House, Light
from sqlalchemy.exc import SQLAlchemyError
from datetime import time
import json

openBlinds = time(8,0)
closeBlinds = time(21,0)
groundFloor = [
    "Wohnzimmer",
    "Esszimmer",
    "Küche",
    "Flur"
]
firstFloor = [
    "Büro1",
    "Büro2",
    "Herrenzimmer"
]


def mainConfig():

    # # create Blinds
    # createBlind(groundFloor[0],1)
    # createBlind(groundFloor[0],2)
    # createBlind(groundFloor[0],3)
    # createBlind(groundFloor[1],4)
    # createBlind(groundFloor[2],5)


    # # Wohnzimmer
      
    # createAutoAction(1,openBlinds,0)
    # createAutoAction(1,closeBlinds,100)

    # createAutoAction(2,openBlinds,0)
    # createAutoAction(2,closeBlinds,100)

    # createAutoAction(3,openBlinds,0)
    # createAutoAction(3,closeBlinds,100)

    # # Schlafzimmer
    
    # createAutoAction(4,openBlinds,0)
    # createAutoAction(4,closeBlinds,100)

    # # Kinderzimmer
      
    # createAutoAction(5,openBlinds,0)
    # createAutoAction(5,closeBlinds,100)

    # Flur

    createLight(groundFloor[3],6,30)
    createLight(groundFloor[3],7,30)


def createAutoAction(port, time_value, closedInPercent):
    try:
        newAction = BlindsActionTimes(port, time_value, closedInPercent)
        db.session.add(newAction)
        db.session.commit()
    except SQLAlchemyError as e:
        print(f"Eintrag '{port} : {time_value}' bereits vorhanden")
        db.session.rollback()

def createBlind(roomName, port):
    try:
        newBlind = Blind(roomName, port)
        db.session.add(newBlind)
        db.session.commit()
    except SQLAlchemyError as e:
        print(f"Eintrag '{port}' bereits vorhanden")
        db.session.rollback()

def createLight(roomName, port, value):
    try:
        newLight = Light(roomName, port, value)
        db.session.add(newLight)
        db.session.commit()
    except SQLAlchemyError as e:
        print(f"Eintrag '{port}' bereits vorhanden")
        db.session.rollback()

def cacheModules():
    data = {}
    # for light in Light.query.get



def doSomething():
    pass



    


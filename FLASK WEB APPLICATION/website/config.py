from . import db
from .models import Blind, BlindsActionTimes, Home
from sqlalchemy.exc import SQLAlchemyError
from datetime import time

openBlinds = time(8,0)
closeBlinds = time(21,0)
rooms = [
    "Wohnzimmer",
    "Schlafzimmer",
    "Kinderzimmer"
]


def mainConfig():

    def firstStart():
        # create Blinds
        testCreateBlind(rooms[0],1)
        testCreateBlind(rooms[0],2)
        testCreateBlind(rooms[0],3)
        testCreateBlind(rooms[1],4)
        testCreateBlind(rooms[2],5)

        # Wohnzimmer
            #open
        createAutoAction(1,openBlinds,0)
        createAutoAction(2,openBlinds,0)
        createAutoAction(3,openBlinds,0)
            #close
        createAutoAction(1,closeBlinds,100)
        createAutoAction(2,closeBlinds,100)
        createAutoAction(3,closeBlinds,100)

        # Schlafzimmer
            #open
        createAutoAction(4,openBlinds,0)
            #close
        createAutoAction(4,closeBlinds,100)

        # Kinderzimmer
            #open
        createAutoAction(5,openBlinds,0)
            #close
        createAutoAction(5,closeBlinds,100)

    # firstStart()




def testCreateBlind(room, port): 
    testBlind = Blind(room, port)
    db.session.add(testBlind)
    db.session.commit()

def createAutoAction(port, time_value, closedInPercent):
    try:
        newAction = BlindsActionTimes(port, time_value, closedInPercent)
        db.session.add(newAction)
        db.session.commit()
    except SQLAlchemyError as e:
        print("Eintrag bereits vorhanden")
        db.session.rollback()


def doSomething():
    pass



    


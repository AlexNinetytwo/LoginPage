from . import db
from .models import Blind, BlindsAutoActions
from sqlalchemy.exc import SQLAlchemyError


def testCreateBlind(room, port): 
    testBlind = Blind(room, port)
    db.session.add(testBlind)
    db.session.commit()

def chreateAutoAction(blind_id, time_value, closedInPercent):
    try:
        newAction = BlindsAutoActions(blind_id, time_value, closedInPercent)
        db.session.add(newAction)
        db.session.commit()
    except SQLAlchemyError as e:
        print("Eintrag bereits vorhanden")
        db.session.rollback()
    


    


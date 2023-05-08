from . import db
from .models import Blind, BlindsAutoActions


def testCreateBlind(room, port): 
    testBlind = Blind(room, port)
    db.session.add(testBlind)
    db.session.commit()

def chreateAutoAction(blind_id, time_value, closedInPercent):
    newAction = BlindsAutoActions(blind_id, time_value, closedInPercent)
    db.session.add(newAction)
    db.session.commit()
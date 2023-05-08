from . import db
from flask_login import UserMixin



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    pin = db.Column(db.String(6))


class Blind(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    room = db.Column(db.String(15))
    closedInPercent = db.Column(db.Integer)
    port = db.Column(db.Integer, unique=True)

    actionTimes = db.relationship('BlindsAutoActions', backref='blind', lazy=True) # Beziehung

    def __init__(self, room, port):
        self.room = room
        self.port = port
        self.closedInPercent = 0

    def raiseTheBlind(self):
        percent = 0
        self.closedInPercent = percent

    def lowerTheBlind(self):
        percent = 0
        self.closedInPercent = percent
    
class BlindsAutoActions(db.Model):

    blind_id = db.Column(db.Integer, db.ForeignKey('blind.id'), primary_key=True) # Beziehung
    time_value = db.Column(db.Time, primary_key=True)
    closedInPercent = db.Column(db.Integer)

    def __init__(self, blind_id, time_value, closedInPercentInPercent):
        self.blind_id = blind_id
        self.time_value = time_value
        self.closedInPercentInPercent = closedInPercentInPercent
        
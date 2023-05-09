from . import db
from flask_login import UserMixin


# Benutzer
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    pin = db.Column(db.String(6))

# Haus
class Home():
    def __init__(self, roomNames:list):
        self.rooms = []
        for roomName in roomNames:
            self.rooms.append(Room(roomName))

    def raiseAllBlinds(self):
        for room in self.rooms:
            room.raiseAllBlinds()

    def lowerAllBlinds(self):
        for room in self.rooms:
            room.raiseAllBlinds()

# Raum
class Room():
    def __init__(self, name):
        self.name = name
        self.blinds = Blind.query.filter_by(room=self.name)

    def raiseAllBlinds(self):
        for blind in self.blinds:
            blind.raiseTheBlind()

    def lowerAllBlinds(self):
        for blind in self.blinds:
            blind.lowerTheBlind()

# Rollo
class Blind(db.Model):

    port = db.Column(db.Integer, primary_key=True)
    room = db.Column(db.String(15))
    

    actionTimes = db.relationship('BlindsActionTimes', backref='blind', lazy=True) # Beziehung zu Action

    def __init__(self, room, port):
        self.room = room
        self.port = port
        self.closedInPercent = 0

    def raiseTheBlind(self):
        percent = 0
        self.closedInPercent = percent

    def lowerTheBlind(self):
        percent = 100
        self.closedInPercent = percent

# Automatikzeiten
class BlindsActionTimes(db.Model):

    port = db.Column(db.Integer, db.ForeignKey('blind.port'), primary_key=True) # Beziehung zu Rollo
    time_value = db.Column(db.Time, primary_key=True)
    closedInPercent = db.Column(db.Integer)

    def __init__(self, port, time_value, closedInPercent):
        self.port = port
        self.time_value = time_value
        self.closedInPercent = closedInPercent
        
from . import db
from flask_login import UserMixin


# Benutzer
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    pin = db.Column(db.String(6))

# Haus
class House(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), unique=True)

    floors = db.relationship('Floor', backref='house', lazy=True)

    def __init__(self, name):
        self.floors = Floor.query.filter_by(house_id=id)

    def getFloors(self):
        self.floors = Floor.query.filter_by(house_id=id)
        return self.floors

    def raiseAllBlinds(self):
        for floor in self.floors:
            floor.raiseAllBlinds()

    def lowerAllBlinds(self):
        for floor in self.floors:
            floor.lowerAllBlinds()

    def lightsOn(self):
        for floor in self.floors:
            floor.lightsOn()

    def lightsOff(self):
        for floor in self.floors:
            floor.lightsOff()

# Etage
class Floor:

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15))
    house_id = db.Column(db.Integer, db.ForeignKey('house.id'))

    rooms = db.relationship('Room', backref='floor', lazy=True)

    def __init__(self, name, house_id):
        self.name = name
        self.house_id = house_id
        self.rooms = Room.query.filter_by(floor_id=id)

    def getRooms(self):
        self.rooms = Room.query.filter_by(floor_id=id)
        return self.rooms

    def raiseAllBlinds(self):
        for room in self.rooms:
            room.raiseAllBlinds()

    def lowerAllBlinds(self):
        for room in self.rooms:
            room.raiseAllBlinds()

    def lightsOn(self):
        for room in self.rooms:
            room.lightsOn()

    def lightsOff(self):
        for room in self.rooms:
            room.lightsOff()

# Raum
class Room(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15))
    floor_id = db.Column(db.Integer, db.ForeignKey('floor.id'))
    
    lights = db.relationship('Light', backref='room', lazy=True)
    blinds = db.relationship('Blind', backref='room', lazy=True)

    def __init__(self, name, floor_id):
        self.name = name
        self.floor_id = floor_id
        self.blinds = Blind.query.filter_by(room_id=id)
        self.lights = Light.query.filter_by(room_id=id)

    def getBlinds(self):
        self.blinds = Blind.query.filter_by(room_id=id)
        return self.blinds

    def getLights(self):
        self.lights = Light.query.filter_by(room_id=id)
        return self.lights

    def raiseAllBlinds(self):
        for blind in self.blinds:
            blind.raiseTheBlind()

    def lowerAllBlinds(self):
        for blind in self.blinds:
            blind.lowerTheBlind()

    def lightsOn(self):
        for light in self.lights:
            light.turnOn()

    def lightsOff(self):
        for light in self.lights:
            light.turnOff()

# Licht
class Light(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
    threshold = db.Column(db.Integer)
    port = db.Column(db.Integer, unique=True)

    def __init__(self, room_id, threshold, port):
        self.room_id = room_id
        self.port = port
        self.threshold = threshold

    def setThreshold(self, value:int):
        self.threshold = value
        db.session.commt()

    def turnOn(self):
        pass

    def turnOff(self):
        pass

# Rollo
class Blind(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
    port = db.Column(db.Integer, unique=True)
    
    actionTimes = db.relationship('BlindsActionTimes', backref='blind', lazy=True) # Beziehung zu Action

    def __init__(self, room_id, port):
        self.room_id = room_id
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

    id = db.Column(db.Integer)
    blind_id = db.Column(db.Integer, db.ForeignKey('blind.id'), primary_key=True)
    time_value = db.Column(db.Time, primary_key=True)
    closedInPercent = db.Column(db.Integer)

    def __init__(self, blind_id, time_value, closedInPercent):
        self.blind_id = blind_id
        self.time_value = time_value
        self.closedInPercent = closedInPercent


        
from . import db
from flask_login import UserMixin


# Benutzer
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    pin = db.Column(db.String(6))

# Haus
class House(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), unique=True, nullable=False)

    floors = db.relationship('Floor', backref='house', lazy=True)

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
class Floor(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    house_id = db.Column(db.Integer, db.ForeignKey('house.id'), nullable=False)

    rooms = db.relationship('Room', backref='floor', lazy=True)

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
    name = db.Column(db.String(15), nullable=False)
    autoBlinds = db.Column(db.Boolean, default=True)
    autoLights = db.Column(db.Boolean, default=True)
    floor_id = db.Column(db.Integer, db.ForeignKey('floor.id'), nullable=False)
    
    lights = db.relationship('Light', backref='room', lazy=True)
    blinds = db.relationship('Blind', backref='room', lazy=True)

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
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    threshold = db.Column(db.Integer)
    auto = db.Column(db.Boolean, default=False)
    port = db.Column(db.Integer, unique=True)

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
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)  
    closedInPercent = db.Column(db.Integer)
    auto = db.Column(db.Boolean, default=False)
    port = db.Column(db.Integer, unique=True)
    
    actionTimes = db.relationship('BlindsActionTimes', backref='blind', lazy=True) # Beziehung zu Action

    def raiseTheBlind(self):
        percent = 0
        self.closedInPercent = percent

    def lowerTheBlind(self):
        percent = 100
        self.closedInPercent = percent

# Automatikzeiten
class BlindsActionTimes(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    blind_id = db.Column(db.Integer, db.ForeignKey('blind.id'),nullable=False)
    time_value = db.Column(db.Time, nullable=False)
    closedInPercent = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'time_value': self.time_value.strftime('%H:%M'),
            'closedInPercent': self.closedInPercent,
        }

db.UniqueConstraint(BlindsActionTimes.blind_id, BlindsActionTimes.time_value, name='uq_blind_time')


        
from . import db
from flask_login import UserMixin


# Benutzer
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    pin = db.Column(db.String(6))

# Haus
class House:
    def __init__(self, roomNames:list):
        self.floors = [Floor(roomNames)]

    def addRooms(self, roomNames:list, floorName:str, floorIndex:int=None):

        if type(floorIndex) == None:
            if len(self.floors) == 1:
                self.floors[-1].addRooms(roomNames)
            else:
                self.floors.append(Floor(roomNames, floorName))

        else:
            if floorIndex in list(range(len(self.floors))):
                self.floors[floorIndex].addRooms(roomNames)
            else:
                self.floors.insert(floorIndex, Floor(roomNames, floorName))

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
    def __init__(self, roomNames:list, floorName="Erdgeschoss"):

        self.name = floorName
        self.rooms = []
        for roomName in roomNames:
            self.rooms.append(Room(roomName))

    def addRooms(self, roomNames):
        for roomName in roomNames:
            self.rooms.append(Room(roomName))

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
class Room:
    def __init__(self, name):
        self.name = name
        self.blinds = Blind.query.filter_by(room=self.name)
        self.lights = Light.query.filter_by(room=self.name)

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

    port = db.Column(db.Integer, primary_key=True)
    threshold = db.Column(db.Integer)
    room = db.Column(db.String(15))

    def __init__(self, room, port, threshold):
        self.port = port
        self.room = room
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
        db.session.commit()

    def lowerTheBlind(self):
        percent = 100
        self.closedInPercent = percent
        db.session.commit()

# Automatikzeiten
class BlindsActionTimes(db.Model):

    port = db.Column(db.Integer, db.ForeignKey('blind.port'), primary_key=True) # Beziehung zu Rollo
    time_value = db.Column(db.Time, primary_key=True)
    closedInPercent = db.Column(db.Integer)

    def __init__(self, port, time_value, closedInPercent):
        self.port = port
        self.time_value = time_value
        self.closedInPercent = closedInPercent


        
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
    autoBlinds = db.Column(db.Boolean, default=True)
    autoLights = db.Column(db.Boolean, default=True)

    floors = db.relationship('Floor', backref='house', lazy=True)

    def getLights(self):
        lights = []
        for floor in self.floors:
            for light in floor.getLights():
                lights.append(light)
        return lights
    
    def getBlinds(self):
        blinds = []
        for floor in self.floors:
            for blind in floor.getBlinds():
                blinds.append(blind)
        return blinds
      
    def getFloors(self):
        return Floor.query.filter_by(house_id=self.id)
      
    def getModuleByPort(port):
        module = Light.query.filter_by(port=port).first()
        if not module:
            module = Blind.query.filter_by(port=port).first()
        return module

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

    def switchAutomatic(self, moduleType):
        if moduleType == 'blinds':
            state = self.autoBlinds = False if self.autoBlinds else True
                
        elif moduleType == 'lights':
            state = self.autoLights = False if self.autoLights else True

        for floor in self.getFloors():
            floor.setAutomatic(moduleType, state)


# Etage
class Floor(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    autoBlinds = db.Column(db.Boolean, default=True)
    autoLights = db.Column(db.Boolean, default=True)
    house_id = db.Column(db.Integer, db.ForeignKey('house.id'), nullable=False)

    rooms = db.relationship('Room', backref='floor', lazy=True)
    
    def getLights(self):
        lights = []
        for room in self.rooms:
            for light in room.lights:
                lights.append(light)  
        return lights
    
    def getBlinds(self):
        blinds = []
        for room in self.rooms:
            for blind in room.blinds:
                blinds.append(blind)
        return blinds

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

    def switchAutomatic(self, moduleType):

        if moduleType == 'blinds':
            state = self.autoBlinds = False if self.autoBlinds else True

        elif moduleType == 'lights':
            state = self.autoLights = False if self.autoLights else True

        for room in self.getRooms():
            room.setAutomatic(moduleType, state)

        
    def setAutomatic(self, moduleType, state):
        if moduleType == 'blinds':
            self.autoBlinds = state
        elif moduleType == 'lights':
            self.autoLights = state
        else:
            raise Exception('ModuleType not found')
        
        for room in self.getRooms():
            room.setAutomatic(moduleType, state)
        
            

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
        return self.blinds

    def getLights(self):
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

    def switchAutomatic(self, moduleType):
        if moduleType == 'blinds':
            self.autoBlinds = False if self.autoBlinds else True
        elif moduleType == 'lights':
            self.autoLights = False if self.autoLights else True
            
        db.session.commit()
        
    def setAutomatic(self, moduleType, state):
        if moduleType == 'blinds':
            self.autoBlinds = state

        elif moduleType == 'lights':
            self.autoLights = state

        db.session.commit()


# Licht
class Light(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    threshold = db.Column(db.Integer)
    auto = db.Column(db.Boolean, default=False)
    port = db.Column(db.Integer, unique=True)

    def setThreshold(self, value:int):
        self.threshold = value
        db.session.commit()

    def turnOn(self):
        pass

    def turnOff(self):
        pass

    def switchAutomatic(self):
        self.auto = False if self.auto else True
        db.session.commit()


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

    def switchAutomatic(self):
        self.auto = False if self.auto == True else True
        db.session.commit()

    def addActionTime(self, time_value, closedInPercent):
        for action in self.actionTimes:
            if action.time_value == time_value:
                action.closedInPercent = closedInPercent
                db.session.commit()
                return "overwritten"
           
        actionTime = BlindsActionTimes(blind_id=self.id, time_value=time_value, closedInPercent=closedInPercent)
        db.session.add(actionTime)
        db.session.commit()
        return "saved"

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


        
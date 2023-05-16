from . import db
from .models import *
from datetime import time

openBlinds = time(8,0)
closeBlinds = time(21,0)



def mainConfig():

    myHome = House(name="HomeSystem")
    print(myHome)
    db.session.add(myHome)
    db.session.commit()

    groundFloor = Floor(name="Erdgeschoss",house_id=myHome.id)
    db.session.add(groundFloor)
    db.session.commit()
    firstFloor = Floor(name="1.OG",house_id=myHome.id)
    db.session.add(firstFloor)
    db.session.commit()

    hallway = Room(name="Flur", floor_id=groundFloor.id)
    db.session.add(hallway)
    db.session.commit()
    livingroom = Room(name="Wohnzimmer", floor_id=groundFloor.id)
    db.session.add(livingroom)
    db.session.commit()
    diningroom = Room(name="Esszimmer", floor_id=groundFloor.id)
    db.session.add(diningroom)
    db.session.commit()
    kitchen = Room(name="Küche", floor_id=groundFloor.id)
    db.session.add(kitchen)
    db.session.commit()

    office1 = Room(name="Büro1", floor_id=firstFloor.id)
    db.session.add(office1)
    db.session.commit()
    office2 = Room(name="Büro2", floor_id=firstFloor.id)
    db.session.add(office2)
    db.session.commit()
    mansroom = Room(name="Herrenzimmer", floor_id=firstFloor.id)
    db.session.add(mansroom)
    db.session.commit()

    port = 0

    for i in range(3):
        newMod = Blind(room_id=livingroom.id, port=port)
        db.session.add(newMod)
        db.session.commit()
        port+=1

    for i in range(1):
        newMod = Blind(room_id=diningroom.id, port=port)
        db.session.add(newMod)
        db.session.commit()
        port+=1

    for i in range(2):
        newMod = Blind(room_id=kitchen.id, port=port)
        db.session.add(newMod)
        db.session.commit()
        port+=1

    for i in range(3):
        newMod = Blind(room_id=office1.id, port=port)
        db.session.add(newMod)
        db.session.commit()
        port+=1

    for i in range(2):
        newMod = Blind(room_id=office2.id, port=port)
        db.session.add(newMod)
        db.session.commit()
        port+=1

    for i in range(2):
        newMod = Blind(room_id=mansroom.id, port=port)
        db.session.add(newMod)
        db.session.commit()
        port+=1

    for i in range(3):
        newMod = Light(room_id=hallway.id, port=port)
        db.session.add(newMod)
        db.session.commit()
        port+=1

    




from .models import *
from . import db

def newObject():
  object_ = unnamed()
  db.session.add(object_)
  db.session.commit()
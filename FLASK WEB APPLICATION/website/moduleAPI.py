def driveBlind(port, pos):
    currentPos = getBlindPos(port)
    if pos > currentPos:
        while pos > currentPos:
            # Jalousie bis pos senken
            pass
    elif pos < currentPos:
        while pos < currentPos:
            # Jalousie bis pos heben
            pass
    return "done"

def getBlindPos(port):
    # Abfragen, um wie viel Prozent die Jalousie geschlossen ist
    pass
    return #currentPos


def lightOnOff(port):
    if lightIsOn(port):
        # Schalte Licht aus
        pass
    else:
        # Schalte Licht an
        pass

def lightIsOn(port):
    # Abfrage ob licht an ist
    pass
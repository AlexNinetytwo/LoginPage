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
    return currentPos

def getBlindPos(port):
    # Abfragen, um wie viel Prozent die Jalousie geschlossen ist
    pass
    return #currentPos
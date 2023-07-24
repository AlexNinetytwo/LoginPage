import schedule
import time
from flask import current_app

import datetime

def perform_database_query():
    # Hier kommt dein Code für die Datenbankabfrage
    # Führe die gewünschte Datenbankabfrage durch
    currentTime = datetime.datetime.now().time()
    with current_app.app_context():
        from models import BlindsActionTimes, Blind
        tasks = BlindsActionTimes.query.all()
        for task in tasks:
            if task.time_value == currentTime:
                blind = Blind.query.get(task.blind_id)
                blind.drive(task.closedInPercent)
            


def schedule_database_query():
    # Plane die Datenbankabfrage alle halbe Stunde
    schedule.every(30).minutes.do(perform_database_query)

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

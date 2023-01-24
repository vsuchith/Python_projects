import random
from datetime import datetime, timedelta

def numOfDays(checkedin_date):
    now=datetime.now()
    diff=now-checkedin_date
    return diff.days

def checkinDate():
    day = [i for i in range(1,32)]
    checkin_date = datetime(2021, 12, random.choice(day))
    return checkin_date


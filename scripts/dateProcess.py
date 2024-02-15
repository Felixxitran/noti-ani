from datetime import datetime


def checkToday(time):
    timeSplit = time.split("T")
    date = timeSplit[0]
    time = timeSplit[1]
    now = datetime.now()
    today=now.strftime('%Y-%m-%d')
    if today == date:
        return True
    return False
def checkNotPassed(time):
    now = datetime.now()
    timeSplit = time.split("T")
    date = timeSplit[0]
    time = timeSplit[1]
    times = time.split('-')
    start = times[0]
    newtime = date+'T'+start
    datetime_object = datetime.strptime(newtime, "%Y-%m-%dT%H:%M:%S")
    return datetime_object > now



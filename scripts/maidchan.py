from animation import run_maid_chan
from backend import backend
from dateProcess import checkToday,checkNotPassed
import threading
import time
from datetime import datetime
def activeAnimations(nameOfEvent):
    print('have active animations')
    run_maid_chan(nameOfEvent)
    alarm()

def preProcess():
    events = backend()
    eventToday=list()
    for item in events: 
        time = item[1]
        summary = item[0]
        if checkToday(time) == True and checkNotPassed(time)==True:
            eventToday.append(item)
    print(eventToday)
    return eventToday


def alarm():
    # Infinite Loop 
    print('this is alarm')
    eventToday = preProcess()
    print(eventToday)
    item =[(),()]
    if eventToday!=[]:
        item = eventToday.pop(0)
   
    
    while eventToday!=[] or item != [(),()]:
        
        timeSplit = item[1].split('T')
            
        alarmTime = timeSplit[1].split('-')
        set_alarm_time = alarmTime[0]

        # Wait for one seconds
        time.sleep(1)

        # Get current time
        current_time = datetime.now().strftime("%H:%M:%S")
        print(current_time,set_alarm_time)

        # Check whether set alarm is equal to current time or not
        if current_time == set_alarm_time:
            activeAnimations(item[0])
            # time.sleep(4)
            # if eventToday != []:
            #     item = eventToday.pop() 
                
            # else: 
            #     print('no event to count')
            #     break
    run_maid_chan('没有会议.我先走啊  :3')
    exit()

x = threading.Thread(target=alarm())
x.start()

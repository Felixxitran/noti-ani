import time, threading


StartTime=time.time()


class setInterval :
    def __init__(self,interval,sound) :
        self.interval=interval
        self.action=sound
        self.stopEvent=threading.Event()
        thread=threading.Thread(target=self.__setInterval)
        thread.start()

    def __setInterval(self) :
        nextTime=time.time()+self.interval
        while not self.stopEvent.wait(nextTime-time.time()) :
            nextTime+=self.interval
            self.sound()

    def cancel(self) :
        self.stopEvent.set()



# will stop interval in 5s
# t=threading.Timer(5,inter.cancel)
# t.start()
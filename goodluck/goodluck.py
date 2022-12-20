print("this is shimeji")

import random
import tkinter as tk
import pyautogui
from playsound import playsound 
import threading
import time
from sound import *



cycle = 0



impath = 'goodluck.png'

#setup window and gif construct
window = tk.Tk()
image = tk.PhotoImage(file=impath)
maid_chan_gif = [image for i in range(30)]
print(maid_chan_gif)
#window configuration
window.config(highlightbackground='black')
window.overrideredirect(True)
window.wm_attributes('-transparentcolor','black')
label = tk.Label(window,bd=0,bg='black')
label.pack()
def gif_work(cycle,frames):
 if cycle < len(frames) -1:
  cycle+=1
 else:
  cycle = 0
 return cycle

def update(cycle):
    print(cycle)
    if(cycle==29):
        time.sleep(2)
    if cycle==1:
        t=threading.Timer(0.1,sound)
        t.start()
    frame = maid_chan_gif[cycle]
    cycle = gif_work(cycle,maid_chan_gif)
    window.geometry('785x800+'+'1700'+'+1000')
    label.configure(image=frame)
    window.after(61,update,cycle)



def sound():
    playsound('maidchan_sound.wav')

def run_maid_chan():
    window.after(61,update,cycle)
    window.mainloop()
run_maid_chan()

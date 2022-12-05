print("this is shimeji")

import random
import tkinter as tk
import pyautogui
from playsound import playsound 
import threading
import time
from sound import *


x = 1400
cycle = 0
check = 1
idle_num =[1,2,3,4]
sleep_num = [10,11,12,13,15]
walk_left = [6,7]
walk_right = [8,9]
event_number = random.randrange(1,3,1)
impath = 'maidchan_gif_2_AdobeExpress.gif'

#setup window and gif construct
window = tk.Tk()
maid_chan_gif = [tk.PhotoImage(file=impath,format = 'gif -index %i' %(i)) for i in range(30)]

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
    frame = maid_chan_gif[cycle]
    cycle = gif_work(cycle,maid_chan_gif)
    window.geometry('800x800+'+'1700'+'+1000')
    label.configure(image=frame)
    window.after(63,update,cycle)



def sound():
    playsound('maidchan_sound.wav')

# start action every 0.6s
playsound = 1
while playsound==1: 
    sound()
window.after(63,update,cycle)
window.mainloop()


    

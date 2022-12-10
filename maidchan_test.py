print("this is shimeji")

import random
import tkinter as tk
import pyautogui
from playsound import playsound 
import threading
import time
from sound import *
from PIL import Image, ImageTk


cycle = 0



impath = 'maidchan.gif'

#setup window and gif construct
window = tk.Tk()
maid_chan_gif = ImageTk.PhotoImage(Image.open(impath))
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
    window.geometry('800x800+'+'1700'+'-300')
    label.configure(image=frame)
<<<<<<< HEAD:maidchan_test.py
    window.after(61,update,cycle)
=======
    window.after(62,update,cycle)
>>>>>>> 3a379241f47945e2af8df1aba423f85477aca5be:main.py



def sound():
    playsound('maidchan_sound.wav')

<<<<<<< HEAD:maidchan_test.py
def run_maid_chan():
    window.after(61,update,cycle)
=======
def run():
    window.after(62,update,cycle)
>>>>>>> 3a379241f47945e2af8df1aba423f85477aca5be:main.py
    window.mainloop()

run_maid_chan()
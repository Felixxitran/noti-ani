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

impath = 'finalmaidchan.gif'
maid_chan_gif =[]
#setup window and gif construct
window = tk.Tk()
for i in range(4,155):
    if i<10:
        impath = "finalmaidchan\photo000"+ str(i)+".bmp"
    elif i<100:
        impath = "finalmaidchan\photo00"+ str(i)+".bmp"
    else:
        impath = 'finalmaidchan\photo0'+ str(i)+".bmp"
    image1 = Image.open(impath)
    resized_image= image1.resize((800,500))
    maid_chan_gif.append(ImageTk.PhotoImage(resized_image))
# maid_chan_gif = [tk.PhotoImage(file=impath,format = 'gif -index %i' %(i)) for i in range(74)]
# idle = [tk.PhotoImage(file=impath+'idle.gif',format = 'gif -index %i' %(i)) for i in range(5)]
print('does not have maid chan yet ')
print(maid_chan_gif)
print('has already have maid chan gif')
#window configuration
# window.config(highlightbackground='black')
window.overrideredirect(True)
window.wm_attributes("-topmost", True)
# window.wm_attributes("-disabled", True)
window.wm_attributes('-transparentcolor','black')

# Turn off the window shadow

# Set the root window background color to a transparent color

label = tk.Label(window,bd=0)
label.pack()
def gif_work(cycle,frames):
 if cycle < len(frames) -1:
  cycle+=1
 else:
  cycle = 0
 return cycle

def update(cycle):
    if cycle==1:
        t=threading.Timer(0.1,sound)
        t.start()
    if(cycle==154):
        time.sleep(0.1)
    frame = maid_chan_gif[cycle]
    cycle = gif_work(cycle,maid_chan_gif)
    window.geometry('800x800+'+'1700'+'+960')
    label.configure(image=frame)
    window.after(8,update,cycle)


def sound():
    playsound('finalmaidchan.wav')

def run_maid_chan():
    window.after(10,update,cycle)
    window.mainloop()
run_maid_chan()
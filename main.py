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



impath = 'maid_chan.gif'
maid_chan_gif =[]
#setup window and gif construct
window = tk.Tk()
# for i in range(0,75):
#     if i<10:
#         impath = "maidchan_gif_bmp\y2m00"+ str(i)+".bmp"
#     else:
#         impath = "maidchan_gif_bmp\y2m0"+ str(i)+".bmp"
#     image1 = Image.open(impath)
#     maid_chan_gif.append(ImageTk.PhotoImage(image1))
maid_chan_gif = [tk.PhotoImage(file=impath,format = 'gif -index %i' %(i)) for i in range(74)]
# idle = [tk.PhotoImage(file=impath+'idle.gif',format = 'gif -index %i' %(i)) for i in range(5)]
print(maid_chan_gif)
#window configuration
window.config(highlightbackground='black')
window.overrideredirect(True)
window.wm_attributes("-topmost", True)
# window.wm_attributes("-disabled", True)
window.wm_attributes('-transparentcolor','white')

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
    print(cycle)
    if(cycle==74):
        time.sleep(2)
    if cycle==1:
        t=threading.Timer(0.1,sound)
        t.start()
    frame = maid_chan_gif[cycle]
    cycle = gif_work(cycle,maid_chan_gif)
    window.geometry('800x800+'+'1700'+'+960')
    label.configure(image=frame)
    window.after(20,update,cycle)



def sound():
    playsound('maidchan_sound.wav')

def run_maid_chan():
    window.after(20,update,cycle)
    window.mainloop()
run_maid_chan()
print("this is shimeji")

import random
import tkinter as tk
import tkinter.font 
import pyautogui
from playsound import playsound 
import threading
import time
# from sound import *
from PIL import Image, ImageTk, ImageDraw, ImageFont
from middleWindow import createWindow






def on_click(name,window):
    print("---------------------------------------------------------------------")
    window.destroy()
    createWindow(name)

def gif_work(cycle,frames):
 if cycle < len(frames) -1:
    cycle+=1
 else:
    
    cycle = 0
 return cycle

def update(cycle,name,maid_chan_gif,window,width,height,label):
    if cycle==1:    
        x = threading.Thread(target=sound)
        x.start()
    if(cycle==154): 
        time.sleep(10000)
    frame = maid_chan_gif[cycle]
    cycle = gif_work(cycle,maid_chan_gif)
    window.geometry('800x800+'+str(width-800)+'+' +str(height-500))
    label.configure(image=frame)
    label.bind('<Button-1>', lambda *_: on_click(name,window))
    window.after(20,update,cycle,name,maid_chan_gif,window,width,height,label)


def sound():
    playsound('mp3andwavfile\maidchan.wav')

def run_maid_chan(name):
    print('animation has run bro')
    cycle = 0
    maid_chan_gif =[]
    #setup window and gif construct
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()

    canvas = tk.Canvas(window, width=800, height=500)
    canvas.bind("<Button-1>", on_click)
    for i in range(1,69):
        if i<10:
            impath = "finalmaidchanwithwords\photo00"+ str(i)+".bmp"
        elif i<100:
            impath = "finalmaidchanwithwords\photo0"+ str(i)+".bmp"
        # else:
        #     impath = 'finalmaidchan\photo'+ str(i)+".bmp"
        image1 = Image.open(impath)
        resized_image= image1.resize((800,500))
        maid_chan_gif.append(ImageTk.PhotoImage(resized_image))

    window.overrideredirect(True)
    window.wm_attributes("-topmost", True)
    # window.wm_attributes("-disabled", True)
    window.wm_attributes('-transparentcolor','black')

    label = tk.Label(window,bd=0)
    label.pack()

    window.after(10,update,cycle,name,maid_chan_gif,window,width,height,label)
    window.mainloop()



run_maid_chan('你好！我在线了，祝你今天快乐 :3')
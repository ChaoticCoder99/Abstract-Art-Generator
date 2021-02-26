from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageDraw
from os import getlogin
from random import randint

def rgb():
    return (randint(0,255),randint(0,255),randint(0,255))

def create(*args):
    w_ = width.get()
    h_ = height.get()
    img = Image.new("RGB",(w_,h_),rgb())
    for i in range((w_+h_)//25):
        pos = ((randint(1,w_),randint(1,h_)),(randint(1,w_),randint(1,h_)))
        image = ImageDraw.Draw(img)
        image.line(pos,rgb())
    img.save("C:\\Users\\{}\\Desktop\\Abstract Image.png".format(getlogin()))     

win = Tk()
win.title("Abstract Art Generator")
win.geometry("640x360")

width_text = ttk.Label(win,text="Width: ")
width_text.grid(row=1,column=0)
width = IntVar()
w = Spinbox(win,from_=640,to=1280,textvariable=width)
w.grid(row=1,column=1)

height_text = ttk.Label(win,text="Height:")
height_text.grid(row=2,column=0)
height = IntVar()
h = Spinbox(win,from_=360,to=720,textvariable=height)
h.grid(row=2,column=1)

submit_button = ttk.Button(win,text="Create Image",command=create)
submit_button.grid(row=3,column=0)


win.mainloop()

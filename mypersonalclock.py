#importing improtant libraries
from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("my personal clock")

# defining the actual func
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label (root, font=("ds-digital", 30),background = "black",foreground = "red")
label.pack(anchor='center')
time()

mainloop()

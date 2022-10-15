from cProfile import label
from cgitb import text
from tkinter import *    #The tkinter package (“Tk interface”) is the standard Python interface to the Tcl/Tk GUI toolkit.

#The tkinter.ttk module provides access to the Tk themed widget set.
# The tkinter.ttk module provides access to the Tk themed widget set
#  several tkinter.ttk widgets (Button, Checkbutton, Entry, Frame, Label, LabelFrame, Menubutton, PanedWindow, Radiobutton, Scale and Scrollbar) to automatically replace the Tk widgets
from tkinter.ttk import *


#The strftime() method returns a string representing date and time using date, time or datetime object.
from time import strftime


ui=Tk()
ui.title('Digital Clock')


def Time():
    time=strftime('%H:%M:%S %p')
    label.config(text=time)
    label.after(1000,Time)



label=Label(ui,font=('Digital Display',80),background='black',foreground='cyan')
label.pack(anchor='center')

Time()

mainloop()
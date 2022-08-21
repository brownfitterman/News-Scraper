from tkinter import *
import requests as re
from geopy.geocoders import Nominatim
from tkinter import filedialog as fd
import tkinter.messagebox

def filename_person():
    global filename
    global name_file
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        )
    name_file=filename.split("/")[-1]
    return filename


ws = Tk()

ws.title('')
f = ('Times', 14)
var = Variable()


select_cev_city_neighborhoods=Label(ws,font=f,text="Select  neighborhoods csv ").grid(row=0,column=0)
Button(ws,)


ws.mainloop()

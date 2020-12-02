'''Text Editor'''

from tkinter import *

from tkinter import filedialog

from tkinter import messagebox

from tkinter import colorchooser



import datetime




def line():

    lin = "_" * 60

    text.insert(INSERT,lin)


def date():

    data = datetime.date.today()

    text.insert(INSERT,data)

   

def normal():

    text.config(font = ("Arial", 12))



def bold():

    text.config(font = ("Arial", 12, "bold"))



def underline():

    text.config(font = ("Arial", 12, "underline"))



def italic():

    text.config(font = ("Arial",12,"italic"))

    

def font():

    (triple,color) = askcolor()

    if color:

       text.config(foreground=color)




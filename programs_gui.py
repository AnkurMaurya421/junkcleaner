import Programs as pg
from tkinter import *
import GUI as gui

from tkinter import ttk
class button():
    def __init__(self,name):
        button.name=name
        button.button=Button(text=button.name,command=lambda:pg.uninstall(button.name,button))
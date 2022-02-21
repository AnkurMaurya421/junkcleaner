import GUI
from tkinter import *
import winapps as windows
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox
import programs_gui as pggui
import files_gui as figui

class gui():
    def __init__(self):

        self.window = Tk()                   #CREATE PARENT WINDOW
        self.window.geometry("250x70")       #set size
        self.window.title("CleanByDate")     #program name
        self.window.configure(background="black")
        Button(self.window, text="Uninstall Programs", command=lambda:pggui.openprogramsgui(self)).grid(row=1, column=0,sticky=E)  # create 2 buttons in parent window
        Button(self.window, text="Delete Files", command=lambda:figui.openfilesgui(self)).grid(row=2, column=0, sticky=W)
        self.window.mainloop()         #start program












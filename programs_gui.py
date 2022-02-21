import Programs as pg
from tkinter import *
import GUI as guiprogram

from tkinter import ttk


def openprogramsgui(self):
    print("hello1")
    self.program_window = Toplevel(self.window)  #created 2nd window for programs uninstallation
    self.program_window.title("uninstall programs")  #set title

    self.canvas = Canvas(self.program_window)             # adding canvas to make window scrollable
    self.scroll_y = Scrollbar(self.program_window, orient="vertical", command=self.canvas.yview)
    self.frame = Frame(self.canvas)                       # adding frame inside canvas to hold buttons and widgets

    Label(self.frame, text="Click to uninstall", anchor=CENTER, font="None 16 bold").grid(row=0, column=0,sticky=W)  # adding titles
    Label(self.frame, text="Last used date", font="None 16 bold ").grid(row=0, column=0, sticky=E)

    counter = 1 #initialized row counter
    app_dictionary = pg.get_applications_with_location()
    for i, j in app_dictionary.items():
        button(self, i, counter)  # created button object to hold the name of program and button that is to be unistalled
        Label(self.frame, text=j).grid(row=counter, column=0, sticky=E)  #creating label displaying last access date in front of button
        counter += 1   #increase row counter

                                                                          # put the frame in the canvas
    self.canvas.create_window(0, 0, anchor='nw', window=self.frame)       #create canvas window
      # making sure everything is displayed before configuring the scrollregion
    self.canvas.update_idletasks()
    self.canvas.configure(scrollregion=self.canvas.bbox('all'),
                          yscrollcommand=self.scroll_y.set)
    self.canvas.pack(fill='both', expand=True, side='left')
    self.scroll_y.pack(fill='y', side='right')
class button:               #button class to hold every button information
    def __init__(self,obj,name,counter):
        self.name=name  #set the name of button to application name
        self.button=Button(obj.frame,text=self.name,command=lambda:pg.uninstall(self,obj)).grid(row=counter, column=0, sticky=W)   #put the button into frame and set command function to uninstall the appplication
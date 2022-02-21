import GUI
from tkinter import *
import winapps as windows
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox
import Programs as pg
import programs_gui as pggui

class gui():
    def __init__(self):

        self.window = Tk()                   #CREATE PARENT WINDOW
        self.window.geometry("250x70")       #set size
        self.window.title("CleanByDate")     #program name
        self.window.configure(background="black")
        Button(self.window, text="Uninstall Programs", command=self.openprogramsgui).grid(row=1, column=0,sticky=E)  # create 2 buttons in parent window
        Button(self.window, text="Delete Files", command=self.openfilesgui).grid(row=2, column=0, sticky=W)
        self.window.mainloop()

    def openprogramsgui(self):
        print("hello1")
        self.program_window = Toplevel(self.window)
        self.program_window.title("uninstall programs")

        self.canvas = Canvas(self.program_window)                                                         #adding canvas to make window scrollable
        self.scroll_y = Scrollbar(self.program_window, orient="vertical", command=self.canvas.yview)
        self.frame = Frame(self.canvas)                                                                   #adding frame inside canvas to hold buttons and widgets


        Label(self.frame, text="Click to uninstall", anchor=CENTER, font="None 16 bold").grid(row=0, column=0, sticky=W) #adding titles
        Label(self.frame, text="Last used date", font="None 16 bold ").grid(row=0, column=0, sticky=E)


        counter = 1
        app_dictionary = pg.get_applications_with_location()
        for i, j in app_dictionary.items():
            button(self,i,counter)                                      #created button object to remeber the name of program to be unistalled associated with button
            Label(self.frame,text=j).grid(row=counter, column=0, sticky=E)
            counter += 1
                                                                                # put the frame in the canvas
        self.canvas.create_window(0, 0, anchor='nw', window=self.frame)
                                                                                # make sure everything is displayed before configuring the scrollregion
        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox('all'),
                     yscrollcommand=self.scroll_y.set)
        self.canvas.pack(fill='both', expand=True, side='left')
        self.scroll_y.pack(fill='y', side='right')


    def openfilesgui(self):
        print("hello2")
        '''files_window = Toplevel(self.window)
        files_window.title("Delete Files")'''





class button:
    counter = 1
    app_dictionary = pg.get_applications_with_location()
    def __init__(self,obj,name,counter):
        self.name=name
        self.button=Button(obj.frame,text=self.name,command=lambda:pg.uninstall(self.name)).grid(row=counter, column=0, sticky=W)

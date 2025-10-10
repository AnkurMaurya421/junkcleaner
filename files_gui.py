from tkinter import *
from tkinter import messagebox
import files as fi

def openfilesgui(self):
    self.files_window = Toplevel(self.window)
    self.files_window.title("Delete Files")
    self.files_window.geometry("750x400")

    self.canvas = Canvas(self.files_window)
    self.scroll_y = Scrollbar(self.files_window, orient="vertical", command=self.canvas.yview)
    self.frame = Frame(self.canvas)

    Label(self.frame, text="Click to Delete", anchor=CENTER, font="None 16 bold").grid(row=0, column=0, sticky=W)
    Label(self.frame, text="Size", anchor=CENTER, font="None 16 bold").grid(row=0, column=1)
    Label(self.frame, text="Last used date", font="None 16 bold").grid(row=0, column=2, sticky=E)

    self.canvas.create_window(0, 0, anchor='nw', window=self.frame)

    def on_frame_configure(event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    self.frame.bind("<Configure>", on_frame_configure)

    filesizedictionary, filelocationdictionary, accesstimedictionary = fi.returndic()
    counter = 1
    for key, size in filesizedictionary.items():
        location = filelocationdictionary[key]
        access_time = accesstimedictionary[key]
        DeleteButton(self, key, location, counter)
        Label(self.frame, text=size).grid(row=counter, column=1, sticky=E)
        Label(self.frame, text=access_time).grid(row=counter, column=2, sticky=E)
        counter += 1

    self.canvas.configure(yscrollcommand=self.scroll_y.set)
    self.canvas.pack(fill='both', expand=True, side='left')
    self.scroll_y.pack(fill='y', side='right')

class DeleteButton:
    def __init__(self, obj, name, location, counter):
        self.name = name
        self.location = location
        self.obj = obj
        self.button = Button(obj.frame, text=self.name,
                             command=self.confirm_and_delete)
        self.button.grid(row=counter, column=0, sticky=W)

    def confirm_and_delete(self):

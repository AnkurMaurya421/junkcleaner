from tkinter import *
import files as fi

def openfilesgui(self):

    self.files_window = Toplevel(self.window)    #created new window on top of parent window
    self.files_window.title("Delete Files")    #set title of window
    self.files_window.geometry("750x400")    #set gemoetry
    self.canvas = Canvas(self.files_window)# adding canvas to make window scrollable
    self.scroll_y = Scrollbar(self.files_window, orient="vertical", command=self.canvas.yview)
    self.frame = Frame(self.canvas)  # adding frame inside canvas to hold buttons and widgets
    Label(self.frame, text="Click to Delete", anchor=CENTER, font="None 16 bold").grid(row=0, column=0,sticky=W)  # adding titles
    Label(self.frame, text="Size", anchor=CENTER, font="None 16 bold").grid(row=0, column=1)
    Label(self.frame, text="Last used date", font="None 16 bold ").grid(row=0, column=2, sticky=E)
    self.canvas.create_window(0, 0, anchor='nw', window=self.frame)  # create canvas window
    counter = 1  # initialized row counter
    filesizedictionary,filelocationdictionary,accesstimedictionary = fi.returndic()
    for i, j in filesizedictionary.items():
        button(self,i,filelocationdictionary[i],counter)
        Label(self.frame, text=j).grid(row=counter, column=1,sticky=E)# created button object to hold the name of file and button that will  delete the file
        Label(self.frame, text=accesstimedictionary[i]).grid(row=counter, column=2,sticky=E)  # creating label displaying last access date in front of button
        counter += 1  # increase row counter
    # making sure everything is displayed before configuring the scrollregion
    self.canvas.update_idletasks()
    self.canvas.configure(scrollregion=self.canvas.bbox('all'),
                          yscrollcommand=self.scroll_y.set)
    self.canvas.pack(fill='both', expand=True, side='left')
    self.scroll_y.pack(fill='y', side='right')

class button:               #button class to hold every button information
    def __init__(self,obj,name,location,counter):
        self.name=name            #set the name of button to file or folder name
        self.location=location     #set the location of button to file or folder location
        self.button=Button(obj.frame,text=self.name,command=lambda:fi.deletefile(self.location)).grid(row=counter, column=0, sticky=W)   #put the button into frame and set command function to delete that file or folder
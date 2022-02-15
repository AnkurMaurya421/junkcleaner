from tkinter import *
import winapps as windows
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox
import Programs as pg
import programs_gui as pggui


window = Tk()                   #CREATE PARENT WINDOW
window.geometry("250x70")       #set size
window.title("CleanByDate")     #program name
window.configure(background="black")



def openprogramsgui():
    program_window = Toplevel(window)
    program_window.title("uninstall programs")

    canvas = Canvas(program_window)                                                         #adding canvas to make window scrollable
    scroll_y = Scrollbar(program_window, orient="vertical", command=canvas.yview)
    frame = Frame(canvas)                                                                   #adding frame inside canvas to hold buttons and widgets


    Label(frame, text="Click to uninstall", anchor=CENTER, font="None 16 bold").grid(row=0, column=0, sticky=W) #adding titles
    Label(frame, text="Last used date", font="None 16 bold ").grid(row=0, column=0, sticky=E)



    counter = 1
    app_dictionary = pg.get_applications_with_location()
    for i, j in app_dictionary.items():
        Button(frame,text=i,command=lambda:pg.uninstall(Button.cget('text'))).grid(row=counter, column=0, sticky=W)
        Label(frame, text=j).grid(row=counter, column=0, sticky=E)
        counter += 1
                                                                                # put the frame in the canvas
    canvas.create_window(0, 0, anchor='nw', window=frame)
    # make sure everything is displayed before configuring the scrollregion
    canvas.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox('all'),
                     yscrollcommand=scroll_y.set)
    canvas.pack(fill='both', expand=True, side='left')
    scroll_y.pack(fill='y', side='right')


def openfilesgui():
    files_window = Toplevel(window)
    files_window.title("Delete Files")




Button(window, text="Uninstall Programs", command=openprogramsgui).grid(row=1, column=0, sticky=E) #create 2 buttons in parent window
Button(window, text="Delete Files", command=openfilesgui).grid(row=2, column=0, sticky=W)

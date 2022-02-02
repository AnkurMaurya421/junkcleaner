from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import Programs as pg
window = Tk()
window.geometry("250x70")
window.title("CleanByDate")
window.configure(background="black")
def openprogramsgui():
   program_window=Toplevel(window)
   program_window.title("uninstall programs")
   app_dictionary=pg.get_applications_with_location_and_without_locations()

def openfilesgui():
    files_window = Toplevel(window)
    files_window.title("Delete Files")
Button(window,text="Uninstall Programs",command=openprogramsgui).grid(row=1,column=0,sticky=E)
Button(window,text="Delete Files",command=openfilesgui).grid(row=2,column=0,sticky=W)

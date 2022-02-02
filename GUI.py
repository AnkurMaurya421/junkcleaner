from tkinter import *
from tkinter import ttk
import programs_gui as pgui
import files_gui as fgui
window = Tk()
window.geometry("150x70")
window.title("CleanByDate")
window.configure(background="black")
def openprogramsgui():
    pgui.window2.mainloop()
def openfilesgui():
    fgui.window1.mainloop()
Button(window,text="Uninstall Programs",command=openprogramsgui).grid(row=1,column=0,sticky=E)
Button(window,text="Delete Files",command=openfilesgui).grid(row=2,column=0,sticky=W)
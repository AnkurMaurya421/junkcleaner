from tkinter import *
from tkinter.ttk import *
import programs_gui as pggui
import files_gui as figui

class Gui:
    def __init__(self):
        try:
            self.window = Tk()                   # CREATE PARENT WINDOW
            self.window.geometry("250x70")       # set size
            self.window.title("CleanByDate")     # program name
            self.window.configure(background="black")

            # Buttons
            Button(
                self.window, 
                text="Uninstall Programs", 
                command=lambda: pggui.openprogramsgui(self)
            ).grid(row=1, column=0, sticky=E)

            Button(
                self.window, 
                text="Delete Files", 
                command=lambda: figui.openfilesgui(self)
            ).grid(row=2, column=0, sticky=W)

            self.window.mainloop()  # start program
        except Exception as e:
            print(f"Error occurred: {e}")
            if hasattr(self, "window"):  
                self.window.destroy()  # safely close window

if __name__ == "__main__":
    Gui()

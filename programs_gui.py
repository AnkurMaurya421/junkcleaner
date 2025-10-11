import Programs as pg
from tkinter import *

class ProgramGUI:
    def __init__(self, window):
        self.window = window

    def openprogramsgui(self):
        self.program_window = Toplevel(self.window)
        self.program_window.title("Uninstall Programs")
        self.program_window.geometry("550x400")

        # Scrollable canvas
        self.canvas = Canvas(self.program_window)
        self.scroll_y = Scrollbar(self.program_window, orient="vertical", command=self.canvas.yview)

        self.frame = Frame(self.canvas)

        Label(self.frame, text="Click to Uninstall", font="None 16 bold").grid(row=0, column=0, sticky=W)
        Label(self.frame, text="Last Used Date", font="None 16 bold").grid(row=0, column=1, sticky=E)

        # Fetch apps
        counter = 1
        app_dictionary = pg.get_applications_with_location()

        for name, last_used in app_dictionary.items():
            ProgramButton(self, name, counter)
            Label(self.frame, text=last_used).grid(row=counter, column=1, sticky=E)
            counter += 1

        # Add frame to canvas
        self.canvas.create_window((0, 0), anchor='nw', window=self.frame)
        self.canvas.update_idletasks()

        self.canvas.configure(scrollregion=self.canvas.bbox('all'),
                              yscrollcommand=self.scroll_y.set)

        self.canvas.pack(fill='both', expand=True, side='left')
        self.scroll_y.pack(fill='y', side='right')

        # Keep scroll working when resized
        self.frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))


class ProgramButton:
    def __init__(self, obj, name, counter):
        self.name = name
        Button(obj.frame, text=self.name,
               command=lambda: pg.uninstall(self.name)).grid(row=counter, column=0, sticky=W)

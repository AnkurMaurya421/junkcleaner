import winapps as windows  # module to get list of installed applications and also used to uninstall them
import os  # module to handle files and OS operations
import time  # to convert last access time stamp to readable date and time
from tkinter import messagebox


def get_applications_with_location():  # function to check that which programs have their installed location and uninstall string registered in registry  and return dictionary in which key=application name and value=install location
    applications_with_uninstallstring = {}  # get applications which can be uninstalled with their install location as value

    for application in windows.list_installed():
        if application.uninstall_string is None or application.uninstall_string == "":
            pass
        else:
            applications_with_uninstallstring[application.name] = str(application.install_location)

    for apps in applications_with_uninstallstring:  # get apps with last used time using location
        try:
            applications_with_uninstallstring[apps] = time.ctime(os.stat(applications_with_uninstallstring[
                                                                             apps]).st_mtime)  # used os module to get last used time and converted it to readable date and time format using time module
        except:
            applications_with_uninstallstring[apps] = "None"


    return applications_with_uninstallstring


def uninstall(application_object, main_obj):  # to uninstall and delete button
    try:
        print(application_object.name)
        windows.uninstall(application_object.name)
    except:
        messagebox.showerror("showerror", "Error occured in registry,try unistalling another application  ")
        main_obj.program_window.destroy()  # destroy the program window in case of error
        return

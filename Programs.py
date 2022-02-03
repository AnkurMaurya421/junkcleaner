import winapps as windows   #module to get list of installed applications and also used to uninstall them
import os   #module to handle files and OS operations
import time # to convert last access time stamp to readable date and time


def get_applications_with_location(): #function to check that which programs have their installed location and uninstall string registered in registry  and return dictionary in which key=application name and value=install location
    applications_with_uninstallstring = {}      #get applications which can be uninstalled
    for application in windows.list_installed():
        if application.uninstall_string is None or application.uninstall_string == "":
            pass
        else:
            applications_with_uninstallstring[application.name] = str(application.install_location)
    with_location = applications_with_uninstallstring
    for apps in with_location:
        try:
            with_location[apps] = time.ctime(os.stat(with_location[apps]).st_mtime)
        except:
           with_location[apps] = "None"
    return with_location

import winapps as windows
import os
import time


def get_applications_with_location_and_without_locations():
    applications_with_uninstallstring = {}
    #applications_without_uninstallstring = {}
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

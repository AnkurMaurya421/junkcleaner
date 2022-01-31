import winapps as windows
import os
import time


def get_applications_with_location_and_without_locations():
    applications_with_uninstallstring = {}
    #applications_without_uninstallstring = {}
    for application in windows.list_installed():

        if application.uninstall_string is None or application.uninstall_string == "":
            pass
            #applications_without_uninstallstring[application.name] = application.install_location
        else:
            print(application.install_location)
            applications_with_uninstallstring[application.name] = str(application.install_location)
    return applications_with_uninstallstring


with_location= get_applications_with_location_and_without_locations()
for apps in with_location:
    try:
        path=os.path.join(with_location[apps],apps)
        timestamp = os.path.getmtime(path)
        curr=time.time()
        timestamp=curr-timestamp
        timestamp=timestamp//86400
        print(timestamp,with_location[apps])
        with_location[apps] = time.ctime(os.stat(with_location[apps]).st_atime)
    except:
        with_location[apps] = 0
print(with_location)

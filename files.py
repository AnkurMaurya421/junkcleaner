import os
from pathlib import Path
home = str(Path.home())  # get home directory
homedir=os.listdir(home)
for x in homedir:
    print(os.path.isdir((os.path.join(home,x))),x)
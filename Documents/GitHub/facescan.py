"""auto hello face ms script"""

import os
maxsize = 128

from pywinauto.application import Application as app

fsv = app.Start("mshello.exe")

fsv.InstallDialog.NextButton.Wait('ready', timeout=30).ClickInput()
fsv.InstallDialog.Wait('ready', timeout=30).TypeKeys(os.getcwd() + "\FastStone Image Viewer", with_spaces=True)
fsv.InstallDialog.End.Wait('ready', timeout=30).ClickInput()

fsv.InstallDialog.FinishButton.Wait('ready', timeout=30).ClickInput()


for dirpath, dirs, files in os.walk('.'):
    for file in files: 
        path = os.path.join(dirpath, file)
        if os.stat(path).st_size == maxsize:
            os.remove(path)

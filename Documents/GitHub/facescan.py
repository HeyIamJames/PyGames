"""auto hello face ms script"""

import os
from pywinauto.application import Application as app

fsv = app.Start("mshello.exe")

fsv.InstallDialog.NextButton.Wait('ready', timeout=30).ClickInput()
fsv.InstallDialog.Wait('ready', timeout=30).TypeKeys(os.getcwd() + "\FastStone Image Viewer", with_spaces=True)
fsv.InstallDialog.End.Wait('ready', timeout=30).ClickInput()

fsv.InstallDialog.FinishButton.Wait('ready', timeout=30).ClickInput()

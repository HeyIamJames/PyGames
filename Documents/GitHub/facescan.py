"""auto hello face ms script"""

import os
from pywinauto.application import Application as app

fsv = app.Start("mshello.exe")

fsv.InstallDialog.NextButton.Wait('ready', timeout=30).ClickInput()

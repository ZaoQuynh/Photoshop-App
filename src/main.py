from tkinter import *
from PhotoshopAppUI import *

class PhotoApp:
    def __init__(self):
        self.ui = PhotoshopAppUI()
        self.ui.run()
       
if __name__ == "__main__":
    app = PhotoApp()
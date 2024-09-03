# Python Hello world that creates a popup using TkInter library

from tkinter import *
from tkinter import ttk

tkRootWindow = Tk()  # Create Tk() class, with window tkRootWindow
tkFrame = ttk.Frame(tkRootWindow, padding=10) # Create frame widget inside rkRootWindow
tkFrame.grid() # geometry manager controls where widgets are placed inside frame
ttk.Label(tkFrame, 
          text="Nobody expects the Spanish Inquisition! ").grid(column=0, row=0) # Create text widget
ttk.Button(tkFrame, 
           text="Run away", command=tkRootWindow.destroy).grid(column=1, row=0) # create button widget

tkRootWindow.mainloop() # Run the event loop
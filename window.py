import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image
from widgets import *

MIN_HEIGHT = 100

class main_window():
    widget_bar_icon = []
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("GUI Designer")
        
        self.setup_main_window()
        self.load_widget_bar()
                
    def run(self):
        self.root.mainloop()
    
    def setup_main_window(self):
        self.main_frame = tk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        self.main_frame.grid(row=0, column=0, sticky=("N", "S", "E", "W"))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        
        self.widget_frame = tk.Frame(self.main_frame)
        self.widget_frame.config(bg="blue")
        self.main_frame.add(self.widget_frame, minsize = 60, stretch="always")
        
        self.working_frame = tk.Frame(self.main_frame)
        self.working_frame.config(bg="red")
        self.working_frame.grid(row=0, column=1)
        self.main_frame.add(self.working_frame, minsize = 100, stretch="always")
        
        self.detail_frame = tk.Frame(self.main_frame)
        self.detail_frame.config(bg="yellow")
        self.detail_frame.grid(row=0, column=2)
        self.main_frame.add(self.detail_frame, minsize = 60, stretch="always")
        
    def load_widget_bar(self):
                
        main_window.widget_bar_icon.append(icon_widget(self.widget_frame, 
                                        "resources/icons/null_icon.png", "View", 50, 50))
        
        main_window.widget_bar_icon[0].widget.grid(row = 0, column = 0)
        
        main_window.widget_bar_icon.append(icon_widget(self.widget_frame, 
                                        "resources/icons/null_icon.png", "Text View", 50, 50))
        
        main_window.widget_bar_icon[1].widget.grid(row = 1, column = 0)
    
        return self.root


    



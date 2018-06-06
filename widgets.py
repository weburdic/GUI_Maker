import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image

class icon_widget():
    img = None
    widget = None
    
    def __init__(self, parent, filename, text, w, h):
        self.parent = parent
        self.filename = filename
        self.text = text
        self.w = w
        self.h = h
        self.create_icon_widget()

    def create_icon_widget(self):
        self.widget = ttk.Frame(self.parent)
        self.img = ImageTk.PhotoImage(Image.open(self.filename))
        canvas = tk.Canvas(self.widget, width = self.w, height = self.h) 
        canvas.grid(row = 0, column = 0)
        canvas.create_image(0,0, anchor=tk.NW, image=self.img)
        ttk.Label(self.widget, text = self.text).grid(row = 1, column = 0, sticky=tk.S)


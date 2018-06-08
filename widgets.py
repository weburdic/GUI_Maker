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



class DragManager():
    def add_dragable(self, widget): 
        
        widget.bindtags(("Draggable",) + widget.bindtags())

        widget.bind_class("Draggable","<ButtonPress>", self.on_start)
        widget.bind_class("Draggable","<B1-Motion>", self.on_drag)
        widget.bind_class("Draggable","<ButtonRelease>", self.on_drop)
        #widget.config("Draggable", cursor="hand1")

    def on_start(self, event):
        print("START")
        # you could use this method to create a floating window
        # that represents what is being dragged.
        pass

    def on_drag(self, event):
        print("DRAG")

        # you could use this method to move a floating window that
        # represents what you're dragging
        pass

    def on_drop(self, event):
        print("HELLO")
        # find the widget under the cursor
        x,y = event.widget.winfo_pointerxy()
        target = event.widget.winfo_containing(x,y)
        print(target.winfo_width())
        try:
            target.config(bg="red")
        except:
            pass

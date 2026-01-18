from tkinter import Tk
from tkinter import ttk
from tkinter import StringVar

class Window:
    def __init__(self, size="1280x720"):
        self.size = size
        self.root = Tk()
        self.frame = ttk.Frame(self.root, padding=10)
        
        self.root.geometry(size)
        self.frame.grid()
        
    def add_label(self, text="default text", grid=None):
        try:
            if grid is not None:
                ttk.Label(self.frame, text=text).grid(column=grid[0], row=grid[1])
            else:
                ttk.Label(self.frame, text=text)
        
        except Exception as e:
            print(e)
    
    def add_option_menu(self, options=["a", "b", "c"], grid=None):
        try:
            default_option = options[0]
            self.display_string = StringVar(value=default_option)
            
            if grid is not None:
                ttk.OptionMenu(self.frame, self.display_string, default_option, *options).grid(column=grid[0], row=grid[1])
            else:
                ttk.OptionMenu(self.frame, self.display_string, default_option, *options)
                
        except Exception as e:
            print(e)
    
    def add_button(self, text="default button", command=None, grid=None):
        if command is not None:
            if grid is not None:        
                ttk.Button(self.frame, text=text, command=command).grid(column=grid[0], row=grid[1])
            else:
                ttk.Button(self.frame, text=text, command=command)
    
    def run(self):
        self.frame.mainloop()
    
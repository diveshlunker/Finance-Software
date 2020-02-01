import tkinter as tk

class File(tk.Frame):
    def __init__(self, *args):
        tk.Frame.__init__(self, *args)
    def show(self):
        self.lift()
        
class CreateChart(File):
   def __init__(self, *args):
       File.__init__(self, *args)
       label = tk.Label(self, text="Create Chart")
       label.pack(side="top", fill="both", expand=True)

import tkinter as tk

class File(tk.Frame):
    def __init__(self, *args):
        tk.Frame.__init__(self, *args,bg="black")
    def show(self):
        self.lift()

class Settle(File):
   def __init__(self, *args):
       File.__init__(self, *args)
       label = tk.Label(self, text="Settle")
       label.pack(side="top", fill="both", expand=True)

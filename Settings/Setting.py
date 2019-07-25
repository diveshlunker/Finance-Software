import tkinter as tk


class Setting(tk.Frame):
    def __init__(self, *args):
        tk.Frame.__init__(self, *args)
    def show(self):
        self.lift()

class Username(Setting):
   def __init__(self, *args):
       Setting.__init__(self, *args)
       label = tk.Label(self, text="Username")
       label.pack(side="top", fill="both", expand=True)

class Password(Setting):
   def __init__(self, *args):
       Setting.__init__(self, *args)
       label = tk.Label(self, text="Password")
       label.pack(side="top", fill="both", expand=True)

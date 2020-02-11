import tkinter as tk
import webbrowser
from HelpDesk.Licence import Licence

class Help(tk.Frame):
    def __init__(self, *args):
        tk.Frame.__init__(self, *args)
    def show(self):
        self.lift()

class About(Help):
   def __init__(self, *args):
       Help.__init__(self, *args)
       label = tk.Label(self, text="About")
       label.pack(side="top", fill="both", expand=True)

class Features(Help):
   def __init__(self, *args):
       Help.__init__(self, *args)
       label = tk.Label(self, text="Features")
       label.pack(side="top", fill="both", expand=True)


       
       


class Terms(Help):
   def __init__(self, *args):
       Help.__init__(self, *args)
       label = tk.Label(self, text="Terms")
       label.pack(side="top", fill="both", expand=True)


class Contribute(Help):
   def __init__(self, *args):
       Help.__init__(self, *args)
       label = tk.Label(self, text="Contribute")
       label.pack(side="top", fill="both", expand=True)


class Star(Help):
   def __init__(self, *args):
       Help.__init__(self, *args)
       label = tk.Label(self, text="Star")
       label.pack(side="top", fill="both", expand=True)



import tkinter as tk


class Report(tk.Frame):
    def __init__(self, *args):
        tk.Frame.__init__(self, *args)
    def show(self):
        self.lift()

class Monthly(Report):
   def __init__(self, *args):
       Report.__init__(self, *args)
       label = tk.Label(self, text="MonthLy")
       label.pack(side="top", fill="both", expand=True)

class Broker(Report):
   def __init__(self, *args):
       Report.__init__(self, *args)
       label = tk.Label(self, text="Broker")
       label.pack(side="top", fill="both", expand=True)

class Profit(Report):
   def __init__(self, *args):
       Report.__init__(self, *args)
       label = tk.Label(self, text="Profit")
       label.pack(side="top", fill="both", expand=True)


class BulkRep(Report):
   def __init__(self, *args):
       Report.__init__(self, *args)
       label = tk.Label(self, text="BulkRep")
       label.pack(side="top", fill="both", expand=True)

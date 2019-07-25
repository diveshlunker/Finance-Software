import tkinter as tk


class View(tk.Frame):
    def __init__(self, *args):
        tk.Frame.__init__(self, *args)
    def show(self):
        self.lift()

class MonthLoan(View):
   def __init__(self, *args):
       View.__init__(self, *args)
       label = tk.Label(self, text="MonthLoan")
       label.pack(side="top", fill="both", expand=True)

class Emi(View):
   def __init__(self, *args):
       View.__init__(self, *args)
       label = tk.Label(self, text="Emi")
       label.pack(side="top", fill="both", expand=True)

class Pending(View):
   def __init__(self, *args):
       View.__init__(self, *args)
       label = tk.Label(self, text="Pending")
       label.pack(side="top", fill="both", expand=True)


class Upcoming(View):
   def __init__(self, *args):
       View.__init__(self, *args)
       label = tk.Label(self, text="Upcoming")
       label.pack(side="top", fill="both", expand=True)


class BrokInHand(View):
   def __init__(self, *args):
       View.__init__(self, *args)
       label = tk.Label(self, text="BrokInHand")
       label.pack(side="top", fill="both", expand=True)


class Vehicles(View):
   def __init__(self, *args):
       View.__init__(self, *args)
       label = tk.Label(self, text="Vehicles")
       label.pack(side="top", fill="both", expand=True)


class Rc(View):
   def __init__(self, *args):
       View.__init__(self, *args)
       label = tk.Label(self, text="Rc")
       label.pack(side="top", fill="both", expand=True)


class AllCust(View):
   def __init__(self, *args):
       View.__init__(self, *args)
       label = tk.Label(self, text="AllCust")
       label.pack(side="top", fill="both", expand=True)

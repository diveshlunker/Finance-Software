import tkinter as tk


class File(tk.Frame):
    def __init__(self, *args):
        tk.Frame.__init__(self, *args)
    def show(self):
        self.lift()

class NewLoan(File):
   def __init__(self, *args):
       File.__init__(self, *args)
       label = tk.Label(self, text="New Loan")
       label.pack(side="top", fill="both", expand=True)

class NewInvoice(File):
   def __init__(self, *args):
       File.__init__(self, *args)
       label = tk.Label(self, text="Invoice")
       label.pack(side="top", fill="both", expand=True)

class Settle(File):
   def __init__(self, *args):
       File.__init__(self, *args)
       label = tk.Label(self, text="Settle")
       label.pack(side="top", fill="both", expand=True)


class NewBroker(File):
   def __init__(self, *args):
       File.__init__(self, *args)
       label = tk.Label(self, text="New Broker")
       label.pack(side="top", fill="both", expand=True)


class CreateChart(File):
   def __init__(self, *args):
       File.__init__(self, *args)
       label = tk.Label(self, text="Create Chart")
       label.pack(side="top", fill="both", expand=True)

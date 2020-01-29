import tkinter as tk
import openpyxl
from Edits.LoanAmount import LoanAmt

class Edit(tk.Frame):
    def __init__(self, *args):
        tk.Frame.__init__(self, *args)
    def show(self):
        self.lift()



class Chart(Edit):
   def __init__(self, *args):
       Edit.__init__(self, *args)
       label = tk.Label(self, text="New Loan")
       label.pack(side="top", fill="both", expand=True)



class Receipt(Edit):
   def __init__(self, *args):
       Edit.__init__(self, *args)
       label = tk.Label(self, text="EditReceipts")
       label.pack(side="top", fill="both", expand=True)


class Broker(Edit):
   def __init__(self, *args):
       Edit.__init__(self, *args)
       label = tk.Label(self, text="EditBroker")
       label.pack(side="top", fill="both", expand=True)


class CashBrok(Edit):
   def __init__(self, *args):
       Edit.__init__(self, *args)
       label = tk.Label(self, text="EditCashBrok")
       label.pack(side="top", fill="both", expand=True)

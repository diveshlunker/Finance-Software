import tkinter as tk


class Page(tk.Frame):
    def __init__(self, *args):
        tk.Frame.__init__(self, *args)
    def show(self):
        self.lift()

class Page1(Page):
   def __init__(self, *args):
       Page.__init__(self, *args)
       label = tk.Label(self, text="This is page 1")
       label.pack(side="top", fill="both", expand=True)

class Page2(Page):
   def __init__(self, *args):
       Page.__init__(self, *args)
       label = tk.Label(self, text="This is page 2")
       label.pack(side="top", fill="both", expand=True)

class Page3(Page):
   def __init__(self, *args):
       Page.__init__(self, *args)
       label = tk.Label(self, text="This is page 3")
       label.pack(side="top", fill="both", expand=True)

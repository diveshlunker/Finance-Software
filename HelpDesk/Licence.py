import tkinter as tk
import webbrowser
class Help(tk.Frame):
    def __init__(self, *args):
        tk.Frame.__init__(self, *args)
    def show(self):
        self.lift()

class Licence(Help):
    
    def __init__(self, *args):
        
        Help.__init__(self, *args)
       
        self.labeljName = tk.Label(self, text="Protected by MIT Licence",height=4)
        self.labeljName.grid(row=0,column=4)
        self.buttonSettle = tk.Button(self, text="VIew Licence", fg="green",width=20)
        self.buttonSettle.grid(row=1,column=1,padx=(0,0))
        self.buttonSettle.config(command = self.openlicence)

    def openlicence(self):
        webbrowser.open("https://github.com/diveshlunker/Finance-Software/blob/master/LICENSE",new=1)

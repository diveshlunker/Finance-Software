import tkinter as tk
from Pages.Page import *
from Files.File import *

class MainView(tk.Frame):

    
    
    def __init__(self, *args):

        tk.Frame.__init__(self, *args)

        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        FileLoan = NewLoan(self)
        FileInvoice = NewInvoice(self)
        FileSettle = Settle(self)
        FileBroker = NewBroker(self)
        FileChart = CreateChart(self)
        

        menu = tk.Menu(root)
        root.config(menu=menu)
        subMenu = tk.Menu(menu)
        menu.add_cascade(label="File", menu=subMenu)
        subMenu.add_command(label="New Loan",command=FileLoan.lift)
        subMenu.add_command(label="New Invoice",command=FileInvoice.lift)
        subMenu.add_command(label="Settle Loan",command=FileSettle.lift)
        subMenu.add_command(label="New Broker",command=FileBroker.lift)
        subMenu.add_command(label="Create Chart",command=FileChart.lift)
        
        subMenu.add_separator()
        subMenu.add_command(label="Exit", command=p1.lift)


        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        FileLoan.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        FileInvoice.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        FileSettle.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        FileBroker.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        FileChart.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        



        p1.show()
        

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()

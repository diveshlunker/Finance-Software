#--------------------------------------Finance Software ------------------------------------

#---------------------------------------Importing Files-------------------------------------
import tkinter as tk
from Pages.Page import *
from Files.File import *
from Edits.Edit import *
from Views.View import *
from Reports.Report import *
from Settings.setting import *
from HelpDesk.help import *


#----------------------------------Base of the software------------------------------------
class MainView(tk.Frame):

    def __init__(self, *args):

        tk.Frame.__init__(self, *args)

        #------------------------------Page file invoked and pages called-----------------
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        #--------------------------Files.file invoked and functions called-----------------
        #----------------------------File option in menu bar-------------------------------
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

        #--------------------------Edits.edit invoked and functions called-----------------
        #----------------------------Edit option in menu bar-------------------------------

        editMenu = Menu(menu)
        menu.add_cascade(label="Edit", menu=editMenu)
        editMenu.add_command(label="Chart",command=doNothing)
        editMenu.add_command(label="loan-amount",command=doNothing)
        editMenu.add_command(label="Receipts",command=doNothing)
        editMenu.add_command(label="Broker File",command=doNothing)
        editMenu.add_command(label="Cash with broker",command=doNothing)
        editMenu.add_separator()
        editMenu.add_command(label="Exit", command=doNothing)

        #--------------------------Views.View invoked and functions called-----------------
        #----------------------------View option in menu bar-------------------------------
        viewMenu = Menu(menu)
        menu.add_cascade(label="View", menu=viewMenu)
        viewMenu.add_command(label="Months Loan",command=doNothing)
        viewMenu.add_command(label="EMI Paid",command=doNothing)
        viewMenu.add_command(label="Dues-Pending",command=doNothing)
        viewMenu.add_command(label="Upcoming Dues",command=doNothing)
        viewMenu.add_command(label="Broker in hand cash",command=doNothing)
        viewMenu.add_command(label="Vehicles List",command=doNothing)
        viewMenu.add_command(label="Rc. No",command=doNothing)
        viewMenu.add_command(label="All Customers",command=doNothing)
        viewMenu.add_separator()
        viewMenu.add_command(label="Exit", command=doNothing)

        #--------------------------Reports.report invoked and functions called-----------------
        #----------------------------Reports option in menu bar-------------------------------
        reportMenu = Menu(menu)
        menu.add_cascade(label="Reports", menu=reportMenu)
        reportMenu.add_command(label="Monthly Loans",command=doNothing)
        reportMenu.add_command(label="Broker Wise",command=doNothing)
        reportMenu.add_command(label="Profit of month",command=doNothing)
        reportMenu.add_command(label="Bulk Report",command=doNothing)
        reportMenu.add_separator()
        reportMenu.add_command(label="Exit", command=doNothing)
        
        #--------------------------Settings.Setting invoked and functions called-----------------
        #----------------------------Settings option in menu bar-------------------------------
        settingMenu = Menu(menu)
        menu.add_cascade(label="Settings", menu=settingMenu)
        settingMenu.add_command(label="Change Username",command=doNothing)
        settingMenu.add_command(label="Change Password",command=doNothing)
        settingMenu.add_separator()
        settingMenu.add_command(label="Exit", command=doNothing)
        
        #--------------------------HelpDesk.help invoked and functions called-----------------
        #----------------------------Help option in menu bar---------------------------------
        helpMenu = Menu(menu)
        menu.add_cascade(label="Help", menu=helpMenu)
        helpMenu.add_command(label="About",command=doNothing)
        helpMenu.add_command(label="Features",command=doNothing)
        helpMenu.add_command(label="Licence",command=doNothing)
        helpMenu.add_command(label="Terms and Conditions",command=doNothing)
        helpMenu.add_command(label="Donate",command=doNothing)
        helpMenu.add_command(label="Contribute",command=doNothing)
        helpMenu.add_command(label="Star",command=doNothing)
        helpMenu.add_separator()
        helpMenu.add_command(label="Exit", command=doNothing)


        #----------------Creating containers and setting up the design---------------------
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
        


#-------------------------Making the layout of software and calling MainView----------------
if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    main.config(background='#2b2b2b')
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(str(screen_width)+"x"+str(screen_height))
    root.mainloop()

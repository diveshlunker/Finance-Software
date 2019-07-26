    #--------------------------------------Finance Software ------------------------------------
#---Developer - N.Divesh
#---Licenced Software
#---Copyright held by N.Divesh

#---------------------------------------Importing Files-------------------------------------
import tkinter as tk
from Pages.Page import *
from Files.File import *
from Edits.Edit import *
from Views.View import *
from Reports.Report import *
from Settings.Setting import *
from HelpDesk.Help import *


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

        EditChart = Chart(self)
        EditLoanAmt = LoanAmt(self)
        EditReceipts = Receipt(self)
        EditBroker = Broker(self)
        EditCashBrok = CashBrok(self)

        editMenu = tk.Menu(menu)
        menu.add_cascade(label="Edit", menu=editMenu)
        editMenu.add_command(label="Chart",command=EditChart.lift)
        editMenu.add_command(label="loan-amount",command=EditLoanAmt.lift)
        editMenu.add_command(label="Receipts",command=EditReceipts.lift)
        editMenu.add_command(label="Broker File",command=EditBroker.lift)
        editMenu.add_command(label="Cash with broker",command=EditCashBrok.lift)
        editMenu.add_separator()
        editMenu.add_command(label="Exit", command=p1.lift)

        #--------------------------Views.View invoked and functions called-----------------
        #----------------------------View option in menu bar-------------------------------

        ViewMonthLoan = MonthLoan(self)
        ViewEmi = Emi(self)
        ViewPending = Pending(self)
        ViewUpcoming = Upcoming(self)
        ViewBrokInHand = BrokInHand(self)
        ViewVehicles = Vehicles(self)
        ViewRc = Rc(self)
        ViewAllCust = AllCust(self)
        
        viewMenu = tk.Menu(menu)
        menu.add_cascade(label="View", menu=viewMenu)
        viewMenu.add_command(label="Months Loan",command=ViewMonthLoan.lift)
        viewMenu.add_command(label="EMI Paid",command=ViewEmi.lift)
        viewMenu.add_command(label="Dues-Pending",command=ViewPending.lift)
        viewMenu.add_command(label="Upcoming Dues",command=ViewUpcoming.lift)
        viewMenu.add_command(label="Broker in hand cash",command=ViewBrokInHand.lift)
        viewMenu.add_command(label="Vehicles List",command=ViewVehicles.lift)
        viewMenu.add_command(label="Rc. No",command=ViewRc.lift)
        viewMenu.add_command(label="All Customers",command=ViewAllCust.lift)
        viewMenu.add_separator()
        viewMenu.add_command(label="Exit", command=p1.lift)

        #--------------------------Reports.report invoked and functions called-----------------
        #----------------------------Reports option in menu bar--------------------------------

        ReportMonthly = Monthly(self)
        ReportBroker = Broker(self)
        ReportProfit = Profit(self)
        ReportBulkRep = BulkRep(self)
        
        reportMenu = tk.Menu(menu)
        menu.add_cascade(label="Reports", menu=reportMenu)
        reportMenu.add_command(label="Monthly Loans",command=ReportMonthly.lift)
        reportMenu.add_command(label="Broker Wise",command=ReportBroker.lift)
        reportMenu.add_command(label="Profit of month",command=ReportProfit.lift)
        reportMenu.add_command(label="Bulk Report",command=ReportBulkRep.lift)
        reportMenu.add_separator()
        reportMenu.add_command(label="Exit", command=p1.lift)
        
        #--------------------------Settings.Setting invoked and functions called-----------------
        #----------------------------Settings option in menu bar---------------------------------

        SettingUsername = Username(self)
        SettingPassword = Password(self)
        
        settingMenu = tk.Menu(menu)
        menu.add_cascade(label="Settings", menu=settingMenu)
        settingMenu.add_command(label="Change Username",command=SettingUsername.lift)
        settingMenu.add_command(label="Change Password",command=SettingPassword.lift)
        settingMenu.add_separator()
        settingMenu.add_command(label="Exit", command=p1.lift)
        
        #--------------------------HelpDesk.help invoked and functions called-----------------
        #----------------------------Help option in menu bar----------------------------------

        HelpAbout = About(self)
        HelpFeatures = Features(self)
        HelpLicence = Licence(self)
        HelpTerms = Terms(self)
        HelpContribute = Contribute(self)
        HelpStar = Star(self)
        
        helpMenu = tk.Menu(menu)
        menu.add_cascade(label="Help", menu=helpMenu)
        helpMenu.add_command(label="About",command=HelpAbout.lift)
        helpMenu.add_command(label="Features",command=HelpFeatures.lift)
        helpMenu.add_command(label="Licence",command=HelpLicence.lift)
        helpMenu.add_command(label="Terms and Conditions",command=HelpTerms.lift)
        helpMenu.add_command(label="Contribute",command=HelpContribute.lift)
        helpMenu.add_command(label="Star",command=HelpStar.lift)
        helpMenu.add_separator()
        helpMenu.add_command(label="Exit", command=p1.lift)


        #----------------Creating containers and setting up the design---------------------
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        #---------------------File Handler------------------------------
        
        FileLoan.place(in_=container,x=0,y=0 ,relwidth=1, relheight=1)
        FileInvoice.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        FileSettle.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        FileBroker.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        FileChart.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        #---------------------Edit Handler-------------------------------
         
        EditChart.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        EditLoanAmt.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        EditReceipts.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        EditBroker.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        EditCashBrok.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        #-----------------------View Handler------------------------------

        ViewMonthLoan.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        ViewEmi.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        ViewPending.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        ViewUpcoming.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        ViewBrokInHand.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        ViewVehicles.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        ViewRc.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        ViewAllCust.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        #---------------------------Report Handler-------------------------
        
        ReportMonthly.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        ReportBroker.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        ReportProfit.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        ReportBulkRep.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        #-------------------------Settings Handler--------------------------

        SettingUsername.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        SettingPassword.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        #-------------------------Help Handler-------------------------------

        HelpAbout.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        HelpFeatures.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        HelpLicence.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        HelpTerms.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        HelpContribute.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        HelpStar.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        #-----------------------------Opening Screen--------------------------

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

#------------------------------------------------------------------------------------END----------------------------------------------------------------------------------------------------
#----------------------------------------------------------Developer - N.Divesh------------------------------------------------------

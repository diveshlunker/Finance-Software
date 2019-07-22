from tkinter import *
def doNothing():
    print("Ok, I wont")
root =Tk()


menu = Menu(root)
root.config(menu=menu)
root.geometry("1920x1080")

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Loan",command=doNothing)
subMenu.add_command(label="New Invoice",command=doNothing)
subMenu.add_command(label="Settle Loan",command=doNothing)
subMenu.add_command(label="New Broker",command=doNothing)
subMenu.add_command(label="Create Chart",command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Chart",command=doNothing)
editMenu.add_command(label="loan-amount",command=doNothing)
editMenu.add_command(label="Receipts",command=doNothing)
editMenu.add_command(label="Broker File",command=doNothing)
editMenu.add_command(label="Cash with broker",command=doNothing)
editMenu.add_separator()
editMenu.add_command(label="Exit", command=doNothing)

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

reportMenu = Menu(menu)
menu.add_cascade(label="Reports", menu=reportMenu)
reportMenu.add_command(label="Monthly Loans",command=doNothing)
reportMenu.add_command(label="Broker Wise",command=doNothing)
reportMenu.add_command(label="Profit of month",command=doNothing)
reportMenu.add_command(label="Bulk Report",command=doNothing)
reportMenu.add_separator()
reportMenu.add_command(label="Exit", command=doNothing)

settingMenu = Menu(menu)
menu.add_cascade(label="Settings", menu=settingMenu)
settingMenu.add_command(label="Change Username",command=doNothing)
settingMenu.add_command(label="Change Password",command=doNothing)
settingMenu.add_separator()
settingMenu.add_command(label="Exit", command=doNothing)

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



root.mainloop()


 

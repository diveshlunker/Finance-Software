import tkinter as tk


class File(tk.Frame):
    def __init__(self, *args):
        tk.Frame.__init__(self, *args,bg="black")
    def show(self):
        self.lift()

class NewLoanFiles:
    def Save(self):
        print("Saving")
    def Cancel(self):
        print("Cancelling")
            
class NewLoan(File,NewLoanFiles):
    def __init__(self, *args):
        File.__init__(self, *args)

        labelName = tk.Label(self, text="New Loan",bg="black",fg="white",height=4)
        labelName.grid(row=0,column=3,padx=(200,0))

        #--------------------Line 1 - 3 inputs - name,fname,phno---------------------------
        labelName = tk.Label(self, text="Name:-",bg="black",fg="white",height=4)
        labelName.grid(row=1,column=1,padx=(200,0))
        e11 = tk.Entry(self,width=30)
        e11.grid(row=1,column=2)
        
        labelFname = tk.Label(self, text="Fathers/Husbands Name:-",bg="black",fg="white")
        labelFname.grid(row=1,column=3,padx=(100,0))
        e12 = tk.Entry(self,width=30)
        e12.grid(row=1,column=4)

        labelPhNo = tk.Label(self, text="Phone No:-",bg="black",fg="white")
        labelPhNo.grid(row=1,column=5,padx=(100,0))
        e13 = tk.Entry(self,width=30)
        e13.grid(row=1,column=6)

        #------------------------Line 2 - 1 input - addr line 1,2---------------------------

        labelAddr1 = tk.Label(self, text="Address Line 1:-",bg="black",fg="white",height=4)
        labelAddr1.grid(row=2,column=1,padx=(200,0))
        e21 = tk.Entry(self,width=60)
        e21.grid(row=2,column=2,columnspan=2)

        labelAddr2 = tk.Label(self, text="Address Line 2:-",bg="black",fg="white",height=4)
        labelAddr2.grid(row=2,column=4,padx=(200,0))
        e22 = tk.Entry(self,width=60)
        e22.grid(row=2,column=5,columnspan=2)

        #----------------------------Line 3 - Guarantee Details----------------------------

        labelGName = tk.Label(self, text="Name:-",bg="black",fg="white",height=4)
        labelGName.grid(row=3,column=1,padx=(200,0))
        e31 = tk.Entry(self,width=30)
        e31.grid(row=3,column=2)
        
        labelGFname = tk.Label(self, text="Fathers/Husbands Name:-",bg="black",fg="white")
        labelGFname.grid(row=3,column=3,padx=(100,0))
        e32 = tk.Entry(self,width=30)
        e32.grid(row=3,column=4)

        labelGPhNo = tk.Label(self, text="Phone No:-",bg="black",fg="white")
        labelGPhNo.grid(row=3,column=5,padx=(100,0))
        e33 = tk.Entry(self,width=30)
        e33.grid(row=3,column=6)

        #------------------------Line 4 - 2 input - Gaddr line 1,2---------------------------

        labelGAddr1 = tk.Label(self, text="Address Line 1:-",bg="black",fg="white",height=4)
        labelGAddr1.grid(row=4,column=1,padx=(200,0))
        e41 = tk.Entry(self,width=60)
        e41.grid(row=4,column=2,columnspan=2)

        labelGAddr2 = tk.Label(self, text="Address Line 2:-",bg="black",fg="white",height=4)
        labelGAddr2.grid(row=4,column=4,padx=(200,0))
        e42 = tk.Entry(self,width=60)
        e42.grid(row=4,column=5,columnspan=2)

        #----------------------------Line 5 - Loan Details----------------------------

        labelDate = tk.Label(self, text="Loan Date:-",bg="black",fg="white",height=4)
        labelDate.grid(row=5,column=1,padx=(200,0))
        e51 = tk.Entry(self,width=30)
        e51.grid(row=5,column=2)
        
        labelAmount = tk.Label(self, text="Amount:-",bg="black",fg="white")
        labelAmount.grid(row=5,column=3,padx=(100,0))
        e52 = tk.Entry(self,width=30)
        e52.grid(row=5,column=4)

        labelBroker = tk.Label(self, text="Broker:-",bg="black",fg="white")
        labelBroker.grid(row=5,column=5,padx=(100,0))
        e53 = tk.Entry(self,width=30)
        e53.grid(row=5,column=6)

        #----------------------------Line 6 - Vehicle Info----------------------------

        labelMake = tk.Label(self, text="Make:-",bg="black",fg="white",height=4)
        labelMake.grid(row=6,column=1,padx=(200,0))
        e61 = tk.Entry(self,width=30)
        e61.grid(row=6,column=2)
        
        labelModel = tk.Label(self, text="Model:-",bg="black",fg="white")
        labelModel.grid(row=6,column=3,padx=(100,0))
        e62 = tk.Entry(self,width=30)
        e62.grid(row=6,column=4)

        labelVehNo = tk.Label(self, text="Vehicle No:-",bg="black",fg="white")
        labelVehNo.grid(row=6,column=5,padx=(100,0))
        e63 = tk.Entry(self,width=30)
        e63.grid(row=6,column=6)

        #----------------------------Line 7 - Inputs on Loan----------------------------

        labelChart = tk.Label(self, text="Chart Months:-",bg="black",fg="white",height=4)
        labelChart.grid(row=7,column=1,padx=(200,0))
        e71 = tk.Entry(self,width=30)
        e71.grid(row=7,column=2)
        
        labelInterest = tk.Label(self, text="Interest Rate:-",bg="black",fg="white")
        labelInterest.grid(row=7,column=3,padx=(100,0))
        e72 = tk.Entry(self,width=30)
        e72.grid(row=7,column=4)

        labelDepo = tk.Label(self, text="Deposit:-",bg="black",fg="white")
        labelDepo.grid(row=7,column=5,padx=(100,0))
        e73 = tk.Entry(self,width=30)
        e73.grid(row=7,column=6)

        #----------------------------Line 8 - Documents----------------------------

        labelNoDocs = tk.Label(self, text="No.of Docs:-",bg="black",fg="white",height=4)
        labelNoDocs.grid(row=8,column=1,padx=(200,0))
        e81 = tk.Entry(self,width=30)
        e81.grid(row=8,column=2)

        labelDocs = tk.Label(self, text="Documents List:-",bg="black",fg="white",height=4)
        labelDocs.grid(row=8,column=3,padx=(200,0))
        e82 = tk.Entry(self,width=60)
        e82.grid(row=8,column=4,columnspan=2)

        #----------------------------Line 9 - RC.No----------------------------

        labelRC = tk.Label(self, text="RC No:-",bg="black",fg="white",height=4)
        labelRC.grid(row=9,column=1,padx=(200,0))
        e91 = tk.Entry(self,width=30)
        e91.grid(row=9,column=2)

        #------------------------------Buttons---------------------------------
        buttonSave = tk.Button(self, text="SAVE", fg="green",command=NewLoan.Save(self),width=20)
        buttonSave.grid(row=11,column=3)
        buttonCancel = tk.Button(self, text="CANCEL", fg="red",command=NewLoan.Cancel(self),width=20)
        buttonCancel.grid(row=11,column=4)

        
        



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

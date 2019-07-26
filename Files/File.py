import tkinter as tk


class File(tk.Frame):
    def __init__(self, *args):
        tk.Frame.__init__(self, *args,bg="black")
    def show(self):
        self.lift()
            
class NewLoan(File):
    def __init__(self, *args):
        File.__init__(self, *args)

        self.labeljName = tk.Label(self, text="New Loan",bg="black",fg="white",height=4)
        self.labeljName.grid(row=0,column=3,padx=(200,0))

        #--------------------Line 1 - 3 inputs - name,fname,phno---------------------------
        self.labelName = tk.Label(self, text="Name:-",bg="black",fg="white",height=4)
        self.labelName.grid(row=1,column=1,padx=(200,0))
        self.e11 = tk.Entry(self,width=30)
        self.e11.grid(row=1,column=2)

        self.tkstrvar = tk.StringVar()  # create tk string variable
        self.tkstrvar.set('Nothing is done yet!')
        
        self.labelFname = tk.Label(self, text="Fathers/Husbands Name:-",bg="black",fg="white")
        self.labelFname.grid(row=1,column=3,padx=(100,0))
        self.e12 = tk.Entry(self,width=30)
        self.e12.grid(row=1,column=4)

        self.labelPhNo = tk.Label(self, text="Phone No:-",bg="black",fg="white")
        self.labelPhNo.grid(row=1,column=5,padx=(100,0))
        self.e13 = tk.Entry(self,width=30)
        self.e13.grid(row=1,column=6)

        #------------------------Line 2 - 1 input - addr line 1,2---------------------------

        self.labelAddr1 = tk.Label(self, text="Address Line 1:-",bg="black",fg="white",height=4)
        self.labelAddr1.grid(row=2,column=1,padx=(200,0))
        self.e21 = tk.Entry(self,width=60)
        self.e21.grid(row=2,column=2,columnspan=2)

        self.labelAddr2 = tk.Label(self, text="Address Line 2:-",bg="black",fg="white",height=4)
        self.labelAddr2.grid(row=2,column=4,padx=(200,0))
        self.e22 = tk.Entry(self,width=60)
        self.e22.grid(row=2,column=5,columnspan=2)

        #----------------------------Line 3 - Guarantee Details----------------------------

        self.labelGName = tk.Label(self, text="Name:-",bg="black",fg="white",height=4)
        self.labelGName.grid(row=3,column=1,padx=(200,0))
        self.e31 = tk.Entry(self,width=30)
        self.e31.grid(row=3,column=2)
        
        self.labelGFname = tk.Label(self, text="Fathers/Husbands Name:-",bg="black",fg="white")
        self.labelGFname.grid(row=3,column=3,padx=(100,0))
        self.e32 = tk.Entry(self,width=30)
        self.e32.grid(row=3,column=4)

        self.labelGPhNo = tk.Label(self, text="Phone No:-",bg="black",fg="white")
        self.labelGPhNo.grid(row=3,column=5,padx=(100,0))
        self.e33 = tk.Entry(self,width=30)
        self.e33.grid(row=3,column=6)

        #------------------------Line 4 - 2 input - Gaddr line 1,2---------------------------

        self.labelGAddr1 = tk.Label(self, text="Address Line 1:-",bg="black",fg="white",height=4)
        self.labelGAddr1.grid(row=4,column=1,padx=(200,0))
        self.e41 = tk.Entry(self,width=60)
        self.e41.grid(row=4,column=2,columnspan=2)

        self.labelGAddr2 = tk.Label(self, text="Address Line 2:-",bg="black",fg="white",height=4)
        self.labelGAddr2.grid(row=4,column=4,padx=(200,0))
        self.e42 = tk.Entry(self,width=60)
        self.e42.grid(row=4,column=5,columnspan=2)

        #----------------------------Line 5 - Loan Details----------------------------

        self.labelDate = tk.Label(self, text="Loan Date:-",bg="black",fg="white",height=4)
        self.labelDate.grid(row=5,column=1,padx=(200,0))
        self.e51 = tk.Entry(self,width=30)
        self.e51.grid(row=5,column=2)
        
        self.labelAmount = tk.Label(self, text="Amount:-",bg="black",fg="white")
        self.labelAmount.grid(row=5,column=3,padx=(100,0))
        self.e52 = tk.Entry(self,width=30)
        self.e52.grid(row=5,column=4)

        self.labelBroker = tk.Label(self, text="Broker:-",bg="black",fg="white")
        self.labelBroker.grid(row=5,column=5,padx=(100,0))
        self.e53 = tk.Entry(self,width=30)
        self.e53.grid(row=5,column=6)

        #----------------------------Line 6 - Vehicle Info----------------------------

        self.labelMake = tk.Label(self, text="Make:-",bg="black",fg="white",height=4)
        self.labelMake.grid(row=6,column=1,padx=(200,0))
        self.e61 = tk.Entry(self,width=30)
        self.e61.grid(row=6,column=2)
        
        self.labelModel = tk.Label(self, text="Model:-",bg="black",fg="white")
        self.labelModel.grid(row=6,column=3,padx=(100,0))
        self.e62 = tk.Entry(self,width=30)
        self.e62.grid(row=6,column=4)

        self.labelVehNo = tk.Label(self, text="Vehicle No:-",bg="black",fg="white")
        self.labelVehNo.grid(row=6,column=5,padx=(100,0))
        self.e63 = tk.Entry(self,width=30)
        self.e63.grid(row=6,column=6)

        #----------------------------Line 7 - Inputs on Loan----------------------------

        self.labelChart = tk.Label(self, text="Chart Months:-",bg="black",fg="white",height=4)
        self.labelChart.grid(row=7,column=1,padx=(200,0))
        self.e71 = tk.Entry(self,width=30)
        self.e71.grid(row=7,column=2)
        
        self.labelInterest = tk.Label(self, text="Interest Rate:-",bg="black",fg="white")
        self.labelInterest.grid(row=7,column=3,padx=(100,0))
        self.e72 = tk.Entry(self,width=30)
        self.e72.grid(row=7,column=4)

        self.labelDepo = tk.Label(self, text="Deposit:-",bg="black",fg="white")
        self.labelDepo.grid(row=7,column=5,padx=(100,0))
        self.e73 = tk.Entry(self,width=30)
        self.e73.grid(row=7,column=6)

        #----------------------------Line 8 - Documents----------------------------

        self.labelNoDocs = tk.Label(self, text="No.of Docs:-",bg="black",fg="white",height=4)
        self.labelNoDocs.grid(row=8,column=1,padx=(200,0))
        self.e81 = tk.Entry(self,width=30)
        self.e81.grid(row=8,column=2)

        self.labelDocs = tk.Label(self, text="Documents List:-",bg="black",fg="white",height=4)
        self.labelDocs.grid(row=8,column=3,padx=(200,0))
        self.e82 = tk.Entry(self,width=60)
        self.e82.grid(row=8,column=4,columnspan=2)

        #----------------------------Line 9 - RC.No----------------------------

        self.labelRC = tk.Label(self, text="RC No:-",bg="black",fg="white",height=4)
        self.labelRC.grid(row=9,column=1,padx=(200,0))
        self.e91 = tk.Entry(self,width=30)
        self.e91.grid(row=9,column=2)

        #------------------------------Buttons---------------------------------
        self.buttonSave = tk.Button(self, text="SAVE", fg="green",width=20)
        self.buttonSave.grid(row=11,column=3)
        self.buttonSave.config(command = self.savedata)

        self.buttonCancel = tk.Button(self, text="CANCEL", fg="red",command=NewLoan.Cancel(self),width=20)
        self.buttonCancel.grid(row=11,column=4)
        self.buttonCancel.config(command = self.canceldata)
        

    def savedata(self):
        self.tkstrvar.set(self.e11.get())     # get entry widget content and store it in tk_string variable
        print(self.tkstrvar.get())

    def canceldata(self):
        print("cancelled")

        
        



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

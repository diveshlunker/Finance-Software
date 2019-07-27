import tkinter as tk
import json
from Files.NewInvoices import NewInvoice
from Files.FileChart import CreateChart
from Files.SettleFile import Settle
from Files.FileBroker import NewBroker


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

        self.tke11 = tk.StringVar()  # create tk string variable
        self.tke11.set('Nothing is done yet!')

        
        self.labelFname = tk.Label(self, text="Fathers/Husbands Name:-",bg="black",fg="white")
        self.labelFname.grid(row=1,column=3,padx=(100,0))
        self.e12 = tk.Entry(self,width=30)
        self.e12.grid(row=1,column=4)

        self.tke12 = tk.StringVar()  # create tk string variable
        self.tke12.set('Nothing is done yet!')

        self.labelPhNo = tk.Label(self, text="Phone No:-",bg="black",fg="white")
        self.labelPhNo.grid(row=1,column=5,padx=(100,0))
        self.e13 = tk.Entry(self,width=30)
        self.e13.grid(row=1,column=6)

        self.tke13 = tk.StringVar()  # create tk string variable
        self.tke13.set('Nothing is done yet!')

        #------------------------Line 2 - 1 input - addr line 1,2---------------------------

        self.labelAddr1 = tk.Label(self, text="Address Line 1:-",bg="black",fg="white",height=4)
        self.labelAddr1.grid(row=2,column=1,padx=(200,0))
        self.e21 = tk.Entry(self,width=60)
        self.e21.grid(row=2,column=2,columnspan=2)

        self.tke21 = tk.StringVar()  # create tk string variable
        self.tke21.set('Nothing is done yet!')

        self.labelAddr2 = tk.Label(self, text="Address Line 2:-",bg="black",fg="white",height=4)
        self.labelAddr2.grid(row=2,column=4,padx=(200,0))
        self.e22 = tk.Entry(self,width=60)
        self.e22.grid(row=2,column=5,columnspan=2)

        self.tke22 = tk.StringVar()  # create tk string variable
        self.tke22.set('Nothing is done yet!')
        #----------------------------Line 3 - Guarantee Details----------------------------

        self.labelGName = tk.Label(self, text="Name:-",bg="black",fg="white",height=4)
        self.labelGName.grid(row=3,column=1,padx=(200,0))
        self.e31 = tk.Entry(self,width=30)
        self.e31.grid(row=3,column=2)

        self.tke31 = tk.StringVar()  # create tk string variable
        self.tke31.set('Nothing is done yet!')
        
        self.labelGFname = tk.Label(self, text="Fathers/Husbands Name:-",bg="black",fg="white")
        self.labelGFname.grid(row=3,column=3,padx=(100,0))
        self.e32 = tk.Entry(self,width=30)
        self.e32.grid(row=3,column=4)

        self.tke32 = tk.StringVar()  # create tk string variable
        self.tke32.set('Nothing is done yet!')

        self.labelGPhNo = tk.Label(self, text="Phone No:-",bg="black",fg="white")
        self.labelGPhNo.grid(row=3,column=5,padx=(100,0))
        self.e33 = tk.Entry(self,width=30)
        self.e33.grid(row=3,column=6)

        self.tke33 = tk.StringVar()  # create tk string variable
        self.tke33.set('Nothing is done yet!')

        #------------------------Line 4 - 2 input - Gaddr line 1,2---------------------------

        self.labelGAddr1 = tk.Label(self, text="Address Line 1:-",bg="black",fg="white",height=4)
        self.labelGAddr1.grid(row=4,column=1,padx=(200,0))
        self.e41 = tk.Entry(self,width=60)
        self.e41.grid(row=4,column=2,columnspan=2)

        self.tke41 = tk.StringVar()  # create tk string variable
        self.tke41.set('Nothing is done yet!')

        self.labelGAddr2 = tk.Label(self, text="Address Line 2:-",bg="black",fg="white",height=4)
        self.labelGAddr2.grid(row=4,column=4,padx=(200,0))
        self.e42 = tk.Entry(self,width=60)
        self.e42.grid(row=4,column=5,columnspan=2)

        self.tke42 = tk.StringVar()  # create tk string variable
        self.tke42.set('Nothing is done yet!')

        #----------------------------Line 5 - Loan Details----------------------------

        self.labelDate = tk.Label(self, text="Loan Date:-",bg="black",fg="white",height=4)
        self.labelDate.grid(row=5,column=1,padx=(200,0))
        self.e51 = tk.Entry(self,width=30)
        self.e51.grid(row=5,column=2)

        self.tke51 = tk.StringVar()  # create tk string variable
        self.tke51.set('Nothing is done yet!')
        
        self.labelAmount = tk.Label(self, text="Amount:-",bg="black",fg="white")
        self.labelAmount.grid(row=5,column=3,padx=(100,0))
        self.e52 = tk.Entry(self,width=30)
        self.e52.grid(row=5,column=4)

        self.tke52 = tk.StringVar()  # create tk string variable
        self.tke52.set('Nothing is done yet!')

        self.labelBroker = tk.Label(self, text="Broker:-",bg="black",fg="white")
        self.labelBroker.grid(row=5,column=5,padx=(100,0))
        self.e53 = tk.Entry(self,width=30)
        self.e53.grid(row=5,column=6)

        self.tke53 = tk.StringVar()  # create tk string variable
        self.tke53.set('Nothing is done yet!')

        #----------------------------Line 6 - Vehicle Info----------------------------

        self.labelMake = tk.Label(self, text="Make:-",bg="black",fg="white",height=4)
        self.labelMake.grid(row=6,column=1,padx=(200,0))
        self.e61 = tk.Entry(self,width=30)
        self.e61.grid(row=6,column=2)

        self.tke61 = tk.StringVar()  # create tk string variable
        self.tke61.set('Nothing is done yet!')
        
        self.labelModel = tk.Label(self, text="Model:-",bg="black",fg="white")
        self.labelModel.grid(row=6,column=3,padx=(100,0))
        self.e62 = tk.Entry(self,width=30)
        self.e62.grid(row=6,column=4)

        self.tke62 = tk.StringVar()  # create tk string variable
        self.tke62.set('Nothing is done yet!')

        self.labelVehNo = tk.Label(self, text="Vehicle No:-",bg="black",fg="white")
        self.labelVehNo.grid(row=6,column=5,padx=(100,0))
        self.e63 = tk.Entry(self,width=30)
        self.e63.grid(row=6,column=6)

        self.tke63 = tk.StringVar()  # create tk string variable
        self.tke63.set('Nothing is done yet!')

        #----------------------------Line 7 - Inputs on Loan----------------------------

        self.labelChart = tk.Label(self, text="Chart Months:-",bg="black",fg="white",height=4)
        self.labelChart.grid(row=7,column=1,padx=(200,0))
        self.e71 = tk.Entry(self,width=30)
        self.e71.grid(row=7,column=2)

        self.tke71 = tk.StringVar()  # create tk string variable
        self.tke71.set('Nothing is done yet!')
        
        self.labelInterest = tk.Label(self, text="Interest Rate:-",bg="black",fg="white")
        self.labelInterest.grid(row=7,column=3,padx=(100,0))
        self.e72 = tk.Entry(self,width=30)
        self.e72.grid(row=7,column=4)

        self.tke72 = tk.StringVar()  # create tk string variable
        self.tke72.set('Nothing is done yet!')

        self.labelDepo = tk.Label(self, text="Deposit:-",bg="black",fg="white")
        self.labelDepo.grid(row=7,column=5,padx=(100,0))
        self.e73 = tk.Entry(self,width=30)
        self.e73.grid(row=7,column=6)

        self.tke73 = tk.StringVar()  # create tk string variable
        self.tke73.set('Nothing is done yet!')

        #----------------------------Line 8 - Documents----------------------------

        self.labelNoDocs = tk.Label(self, text="No.of Docs:-",bg="black",fg="white",height=4)
        self.labelNoDocs.grid(row=8,column=1,padx=(200,0))
        self.e81 = tk.Entry(self,width=30)
        self.e81.grid(row=8,column=2)

        self.tke81 = tk.StringVar()  # create tk string variable
        self.tke81.set('Nothing is done yet!')

        self.labelDocs = tk.Label(self, text="Documents List:-",bg="black",fg="white",height=4)
        self.labelDocs.grid(row=8,column=3,padx=(200,0))
        self.e82 = tk.Entry(self,width=60)
        self.e82.grid(row=8,column=4,columnspan=2)

        self.tke82 = tk.StringVar()  # create tk string variable
        self.tke82.set('Nothing is done yet!')

        #----------------------------Line 9 - RC.No----------------------------

        self.labelRC = tk.Label(self, text="RC No:-",bg="black",fg="white",height=4)
        self.labelRC.grid(row=9,column=1,padx=(200,0))
        self.e91 = tk.Entry(self,width=30)
        self.e91.grid(row=9,column=2)

        self.tke91 = tk.StringVar()  # create tk string variable
        self.tke91.set('Nothing is done yet!')

        #------------------------------Buttons---------------------------------
        self.buttonSave = tk.Button(self, text="SAVE", fg="green",width=20)
        self.buttonSave.grid(row=11,column=3)
        self.buttonSave.config(command = self.savedata)

        self.buttonCancel = tk.Button(self, text="CANCEL", fg="red",width=20)
        self.buttonCancel.grid(row=11,column=4)
        self.buttonCancel.config(command = self.canceldata)

        #------------------------Opening File in append mode--------------------
        self.FileOpen = open("loanfile.txt","a")
        self.d={}
        

    def savedata(self):

        #--------------------------------------------------Getting all the entries and saving in a particular variable and thereby saving in database---------------------------------------
        
        self.tke11.set(self.e11.get())     
        k11=self.tke11.get()
        self.d["custname"]=k11

        self.tke12.set(self.e12.get())
        k12 = self.tke12.get()
        self.d["custfname"]=k12

        
        self.tke13.set(self.e13.get())
        k13 = self.tke13.get()
        self.d["custphno"]=k13
        
        self.tke21.set(self.e21.get())
        k21 = self.tke21.get()
        self.d["add1"]=k21
        
        self.tke22.set(self.e22.get())
        k22 = self.tke22.get()
        self.d["add2"]=k22
        
        self.tke31.set(self.e31.get())
        k31 = self.tke31.get()
        self.d["gauname"]=k31
        
        self.tke32.set(self.e32.get())
        k32 = self.tke32.get()
        self.d["gaufname"]=k32
        
        self.tke33.set(self.e33.get())
        k33 = self.tke33.get()
        self.d["gauphno"]=k33
        
        self.tke41.set(self.e41.get())
        k41 = self.tke41.get()
        self.d["gadd1"]=k41
        
        self.tke42.set(self.e42.get())
        k42 = self.tke42.get()
        self.d["gadd2"]=k42
        
        self.tke53.set(self.e53.get())
        k53 = self.tke53.get()
        self.d["broker"]=k53
        
        self.tke52.set(self.e52.get())
        k52 = self.tke52.get()
        self.d["amount"]=k52
        
        self.tke51.set(self.e51.get())
        k51 = self.tke51.get()
        self.d["ldate"]=k51
        
        self.tke61.set(self.e61.get())
        k61 = self.tke61.get()
        self.d["make"]=k61
        
        self.tke62.set(self.e62.get())
        k62 = self.tke62.get()
        self.d["model"]=k62
        
        self.tke63.set(self.e63.get())
        k63 = self.tke63.get()
        self.d["vehno"]=k63
        
        self.tke71.set(self.e71.get())
        k71 = self.tke71.get()
        self.d["cmonths"]=k71
        
        self.tke72.set(self.e72.get())
        k72 = self.tke72.get()
        self.d["irate"]=k72
        
        self.tke73.set(self.e73.get())
        k73 = self.tke73.get()
        self.d["deposit"]=k73
        
        self.tke81.set(self.e81.get())
        k81 = self.tke81.get()
        self.d["nodocs"]=k81

        self.tke82.set(self.e82.get())
        k82 = self.tke82.get()
        self.d["docslist"]=k82
        
        self.tke91.set(self.e91.get())
        k91 = self.tke91.get()
        self.d["rcno"]=k91
        
        #-------------------------------------Writing json file by converting it from dictionary to a file--------------------------------------------
        self.FileOpen.write(json.dumps(self.d))
        self.FileOpen.write("\n")
        self.FileOpen.close()
        self.canceldata()
        self.e11.delete(0, 'end')
        self.popupmsg("Data Saved !!")

        #---------------------------Data successfully saved-----------------------------------


    def canceldata(self):

        

        #----------------------Clearing all the entries---------------------------
        self.e11.delete(0, 'end')
        self.e12.delete(0, 'end')
        self.e13.delete(0, 'end')
        self.e21.delete(0, 'end')
        self.e22.delete(0, 'end')
        self.e31.delete(0, 'end')
        self.e32.delete(0, 'end')
        self.e33.delete(0, 'end')
        self.e41.delete(0, 'end')
        self.e42.delete(0, 'end')
        self.e51.delete(0, 'end')
        self.e52.delete(0, 'end')
        self.e53.delete(0, 'end')
        self.e61.delete(0, 'end')
        self.e62.delete(0, 'end')
        self.e63.delete(0, 'end')
        self.e71.delete(0, 'end')
        self.e72.delete(0, 'end')
        self.e73.delete(0, 'end')
        self.e81.delete(0, 'end')
        self.e82.delete(0, 'end')
        self.e91.delete(0, 'end')

        #----------------------------since the file was closed, reopening the file------------------------------------
        
        print("cancelled")
        self.FileOpen = open("loanfile.txt","a")
        
    def popupmsg(self,msg):
        LARGE_FONT= ("Verdana", 12)
        NORM_FONT = ("Helvetica", 10)
        SMALL_FONT = ("Helvetica", 8)
        popup = tk.Tk()
        popup.wm_title("!")
        label = tk.Label(popup, text=msg, font=NORM_FONT)
        label.pack(side="top", fill="x", pady=10)
        B1 = tk.Button(popup, text="Okay", command = popup.destroy)
        B1.pack()
        popup.mainloop()

        









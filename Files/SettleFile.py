import tkinter as tk
import json
import uuid
import os


class File(tk.Frame):
    def __init__(self, *args):
        tk.Frame.__init__(self, *args,bg="black")
    def show(self):
        self.lift()
            
class Settle(File):
    def __init__(self, *args):
        File.__init__(self, *args)


        self.labeljName = tk.Label(self, text="New Loan",bg="black",fg="white",height=4)
        self.labeljName.grid(row=0,column=3,padx=(200,0))

        self.SetVehNo = tk.Label(self, text="VehNo:-",bg="black",fg="white",height=4)
        self.SetVehNo.grid(row=1,column=1,padx=(200,0))
        self.e11 = tk.Entry(self,width=30)
        self.e11.grid(row=1,columnspan=2,column=2)
        
        self.tke11 = tk.StringVar()  # create tk string variable
        self.tke11.set('Nothing is done yet!')

        

        self.buttonSettle = tk.Button(self, text="SAVE", fg="green",width=20)
        self.buttonSettle.grid(row=1,column=4)
        self.buttonSettle.config(command = self.settlefile)

        

    def settlefile(self):
        self.tke11.set(self.e11.get())
        self.setk11 = self.tke11.get()
        print(self.setk11)
        print(self.setk11)
        self.FileOpen = open("Database/CustToUid.txt","r")
        self.f1=self.FileOpen.readlines()
        for i in self.f1:
            i=eval(i)
            print(i["vehno"])
            if(i["vehno"]==str(self.setk11)):
                print("Yeah")
                self.custid = i["uid"]
                self.FileOpenCust = open("Database/Customers/"+self.custid+".txt","r+")
                self.readlinesf1 = self.FileOpenCust.readlines()
                self.d={}
                for j in self.readlinesf1:
                    print(j)
                    j=eval(j)
                    self.d["Name"] = j["Name"]
                    self.d["vehno"] = j["vehno"]
                    self.d["chartMonths"] = j["chartMonths"]
                    self.d["upcomingdue"] = j["upcomingdue"]
                    self.d["ChartStatus"] = "Settled"
                self.FileOpenCust.close()
                self.FileOpenCust = open("Database/Customers/"+self.custid+".txt","w")

                self.FileOpenCust.write(json.dumps(self.d))
                self.FileOpenCust.write("/n")
                self.FileOpenCust.close()
        
            
            
            

        

        











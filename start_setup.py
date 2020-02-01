from pynput import keyboard 
import time
import math
from tkinter import *
import os
from setup import *

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Enter Password to continue", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Enter password", height="2", width="30", command = login).pack()
    Label(text="").pack()
    
    

    main_screen.mainloop()

def delete_login_success():
    print("error")
def success():
    print("loss")



def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")

    def callb(key): #what to do on key-release
        
        ti1 = float(str(time.time() - t)[0:5]) #converting float to str, slicing the float
        l.append(str(key)[1]+str(math.ceil(ti1)))
        print(l)
        
        print("The key",key," is pressed for",ti1,'seconds')
        return False #stop detecting more key-releases
    def callb1(key): #what to do on key-press
        return False #stop detecting more key-presses

    l=[]


    for i in range(6):
       
        
        with keyboard.Listener(on_press = callb1) as listener1: #setting code for listening key-press
            listener1.join()

        t = time.time() #reading time in sec
        

        with keyboard.Listener(on_release = callb) as listener: #setting code for listening key-release
            listener.join()
            
    print(l)
    
    def login_success():
        print("success")
        
        
        os.system("setup.py")
    def password_not_recognised():
        print("error!!")
        Label(login_screen, text="Wrong Password !! Please Try Again", bg="red").pack()
        Label(login_screen, text="").pack()
    
        
    s1 = "".join(l)
    password1=""
    for i in s1:
        password1+=str(ord(i))
    if password1 == "100501054911850101491154910449":
        login_success()

    else:
        password_not_recognised()

    

main_account_screen()


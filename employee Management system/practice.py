# importing tkinter modules
import tkinter as tk
# This module is for combobox
from tkinter import ttk
#This module is for messsge box
from tkinter import messagebox

#this is a main class for login page
class Main(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame=None
        self.title("Welcome")
        self.switch_frame(Login_Screen)
    #for swiching frame
    def switch_frame(self,frame_class):
        new_frame=frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame=new_frame
        self._frame.grid(pady=8,padx=25)
#===============Login Screen=============================================================================
class Login_Screen(tk.Frame):
    def __init__(self,master):
        #This will set name of title background color and size and shape of window
        master.title("Login")
        master.config(bg="#3E5C9A")
        master.geometry("500x330")

        #This will create a frame inside login screen
        tk.Frame.__init__(self,master,bd=4,bg="azure", relief=tk.GROOVE) # creating the frame

        # This will creates a label and adding some features in it
        title = tk.Label(self, text="Login Into system", font=("arial", 20, "bold"),
                      bd=5, relief=tk.FLAT, bg="#3E5C9A",fg="white",padx=40, width=21)
        title.grid(row=0, columnspan=5) # sets the position

        #This will create some empty labels
        self.popup = tk.Label(self, text="", font=("arial", 15), fg="red", bg="azure")
        self.popup.grid(row=1, column=0, columnspan=5,sticky="WE")
        tk.Label(self, text="",bg="azure").grid(row=3)
        # This will create label for username and adding some function
        tk.Label(self,text="Username",font=("arial",15),bg="azure",
                 fg="black").grid(row=4,column=0)
        #This will create  username and password and set the position too
        self.login_username_entry=tk.Entry(self,font=("arial",10),bd=5,width=30,
                                            relief=tk.GROOVE,bg="white")
        self.login_username_entry.grid(row=4,column=1,columnspan=5,sticky="W")
        tk.Label(self, text="",bg="azure").grid(row=5) # making some space
        tk.Label(self, text="Password",font=("arial",15),
                 fg="black",bg="azure").grid(row=6, column=0)
        self.login_password_entry = tk.Entry(self,show="*",font=("arial",10),
                                             width=30, bd=5, relief=tk.GROOVE,bg="white")
        self.login_password_entry.grid(row=6, column=1,columnspan=5,sticky="W")
        tk.Label(self, text="",bg="azure").grid(row=7) # spacing

        # This will create login button and adding some functions
        tk.Button(self,text="Login",font=("arial",15,"bold"),padx=10,bg="green",width=10,fg="white",
                  command=self.login_varification).grid(row=8,column=1,columnspan=1,sticky="WE")
        tk.Label(self, text="",bg="azure").grid(row=9) # spacing

        # This will make register button and functions added wil give their position in login screen
        tk.Button(self, text="REGISTER", font=("arial", 15), padx=10,
                  bg="#3E5C9A",fg="white",width=10,
                  # Here lambda command will switch frame from user login to user register
                  command=lambda : master.switch_frame(User_register)).grid(row=10, column=1,columnspan=1)

#=================login verification=======================================================================
    def login_varification(self): # creating login function to enter the page
        #creating variables for entries
        login_username = str(self.login_username_entry.get())
        login_password = str(self.login_password_entry.get())
        # creating variable for username and password of class User_register()
        username_checking,password_checking=User_register.taking_user_password
        # gives error text in main screen if any entry is empty
        if login_username == "" or login_password == "":
            self.popup["text"]="Enter userId & password to login"
        else:
            for i in range(len(username_checking)):
                if str(username_checking[i]) == login_username and\
                        str(password_checking[i]) == login_password:
                    messagebox.showinfo("Information","Login Successful")
                    self.master.destroy()
                    import Employee_Manage # switching frame to employee page
                    break # stops loop if username and password is matched
                else:
                    self.login_password_entry.delete(0, tk.END) # clears the entered entry
                    self.login_username_entry.delete(0, tk.END)
                    # gives error text in main screen untill username and password are matched
                    if str(username_checking[i]) != login_username and\
                        str(password_checking[i]) != login_password:
                        self.popup["text"] = "Please enter valid UserId and password"

        # creating username and password without registration
        if login_username=="admin" and login_password=="admin":
            self.master.destroy()
            import Employee_Manage

call=Main()
call.mainloop()











































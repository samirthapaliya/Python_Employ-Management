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
        username_checking,password_checking=User_register.taking_user_password(self)
        # gives error text in main screen if any entry is empty
        if login_username == "" or login_password == "":
            self.popup["text"]="Your Entry is empty"
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
            self.popup["text"] = "Please enter valid Username and Password"

        # creating username and password without registration
        if login_username=="admin" and login_password=="admin":
            self.master.destroy()
            import Employee_Manage




#======================Register Page===========================================================================

class User_register(tk.Frame):
    def __init__(self,master):
        # This will sets shape, size, title name and background colour with frame
        master.geometry("750x670+0+0")
        master.title("Create Account")
        master.config(bg="#3E5C9A")
        tk.Frame.__init__(self,master,bg="azure",bd=3,relief=tk.GROOVE)

        # This will create Title of page
        heading = tk.Label(self, text="Create Your Account", font=("Arial", 15, "bold"), fg="white",
                           bd=4,relief=tk.FLAT, bg="#3E5C9A", width=57, height=2)
        heading.grid(row=0, pady=(0, 30), columnspan=7) # sets position
        #This will create a variable for day, month, and year
        self.month = tk.IntVar()
        self.year = tk.IntVar()
        self.day = tk.IntVar()
        self.months = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

        self.days=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
        self.years=(1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,170,1971,1972,1973,1974,1975,
                   1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1988,1989,1990,
                   1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,
                   2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020)
        self.gender=("Male","Female","Other")
        # This will sets position
        tk.Label(self, text="", bg="azure").grid(row=2)

        #This is a Label for First,last name and mobile no.
        tk.Label(self,text="First Name:",bg="azure",pady=10,
                 font=("arial",20),fg="Black").grid(row=3,column=0,sticky="E")
        self.firstname_entry=tk.Entry(self,font=("arial",10),bd=4,relief=tk.GROOVE,bg="azure",width=40)
        self.firstname_entry.grid(row=3,column=1,columnspan=6,sticky="W")

        tk.Label(self, text="Last Name:",bg="azure",pady=10,
                 font=("arial",20),fg="Black").grid(row=4, column=0, pady=(0, 2),sticky="E")
        self.lastname_entry = tk.Entry(self,font=("arial",10),bd=4,relief=tk.GROOVE,bg="azure",width=40)
        self.lastname_entry.grid(row=4, column=1,columnspan=6,sticky="W")

        tk.Label(self, text="Mobile Number:",bg="azure",pady=10,
                 font=("arial", 20), fg="Black").grid(row=5, column=0,sticky="E")
        self.mobile_entry = tk.Entry(self,font=("arial",10),bd=4,relief=tk.GROOVE,bg="azure",width=40)
        self.mobile_entry.grid(row=5,column=1, columnspan=6,sticky="W")
        #This is a Label for Birthday.
        tk.Label(self, text="Birthday", bg="azure", pady=10,
                 font=("arial", 20), fg="Black").grid(row=10, column=0, pady=(0, 2), sticky="E")
        tk.Label(self, text="Day-Month-Year", font=("arial", 10)).grid(row=10, column=1,sticky="W")

        self.day=ttk.Combobox(self, width=11, font=("arial", 10),state="readonly", value=self.days,
                     textvariable=self.day)
        self.day.grid(row=10, column=2,sticky="WE")
        self.month=ttk.Combobox(self, width=10, font=("arial", 10),state="readonly", value=self.months,
                     textvariable=self.month)
        self.month.grid(row=10, column=3,sticky="WE")
        self.year=ttk.Combobox(self, width=10, font=("arial", 10),state="readonly", value=self.years,
                     textvariable=self.year)
        self.year.grid(row=10, column=4,sticky="WE")
        tk.Label(self, text="Gender:", justify=tk.LEFT, pady=10,font=("arial", 20),
                 bg="azure",fg="Black").grid(row=9,column=0,sticky="E")
        self.genders=ttk.Combobox(self,width=30,font=("arial",13),state="readonly",value=self.gender)
        self.genders.grid(row=9,column=1,columnspan=3,sticky="W")
        #This will create username
        tk.Label(self, text="Username:", bg="azure", pady=10,
                 font=("arial", 20), fg="Black").grid(row=6, column=0, sticky="E")
        self.username_entry=tk.Entry(self,font=("arial", 10),bd=4,relief=tk.GROOVE,bg="azure",width=40)
        self.username_entry.grid(row=6, column=1, columnspan=6,sticky="W")
        #This will create password entry
        tk.Label(self, text="Password:", bg="azure", pady=10,
                 font=("arial", 20), fg="Black").grid(row=7, column=0, pady=(0, 2), sticky="E")
        self.password_entry = tk.Entry(self, font=("arial", 10), bd=4, relief=tk.GROOVE, bg="azure",
                                        width=40,show="*")
        self.password_entry.grid(row=7, column=1, columnspan=6,sticky="W")
        #This will create password confirmation entry
        tk.Label(self, text="Conform Password:", bg="azure", pady=11,
                 font=("arial", 20), fg="Black").grid(row=8, column=0, pady=(0, 2), sticky="E")
        self.conform_password_entry = tk.Entry(self, font=("arial", 10), bd=4, relief=tk.GROOVE, bg="azure",
                                        width=40,show="*")
        self.conform_password_entry.grid(row=8, column=1, columnspan=6,sticky="W")


#====================making frame for button===================================================================
       #This will create a frame of button
        btnFrame = tk.Frame(master, bd=4, relief=tk.GROOVE, bg="azure")
        btnFrame.place(x=23, y=580)

        #This is a code for register button
        tk.Button(btnFrame, text="Sign Up", bg="Green",font=("arial", 22,"bold"),width=12,
                  command=self.sign_UP ,fg="white").grid(row=0,column=1,padx=3,pady=3)
        #This will make clear button
        tk.Button(btnFrame, text="Reset",bg="#3E5C9A",font=("arial",22,"bold"),width=12,fg="white",
                  command=self.reset).grid(row=0,column=0,padx=3,pady=3)
        # This will create button for going to login screen
        tk.Button(btnFrame, text="Back", bg="#3E5C9A", font=("arial", 22, "bold"), width=12, fg="white",
                  command=self.back).grid(row=0,column=2,padx=3,pady=3)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=
    # Now adding function to register
    def sign_UP(self):
        # This will create variable for all the entry of data
        username_user = self.username_entry.get()
        password_user = self.password_entry.get()
        conform_user = self.conform_password_entry.get()
        firstname_user = self.firstname_entry.get()
        lastname_user = self.lastname_entry.get()
        mobile_user = self.mobile_entry.get()
        gender_user=self.genders.get()
        day_user=self.day.get()
        month_user=self.month.get()
        year_user=self.year.get()

        username_list_for_checking,password_list_for_checking=self.taking_user_password()

        # This code will make a popup messages for error or sucessfull entry of data
        if username_user=="" or password_user=="" or firstname_user==" " or lastname_user=="" \
                or conform_user=="" or mobile_user=="" or gender_user==""or day_user=="" \
            or month_user=="" or year_user=="":
            messagebox.showerror("Information","All entry must be fill") # popup error message
        # for error message in username
        elif username_user in username_list_for_checking:
            messagebox.showerror("informantion","Username already taken")
        #for error message in lastname
        elif not firstname_user.isalpha() or not lastname_user.isalpha():
            messagebox.showerror("Information","Name accept only alphabet")
        #for error message in movile number
        elif (len(mobile_user)!=10) or (not mobile_user.isdigit):
            messagebox.showerror("Information","Contact entry must be 10 numeric digit")
        # for error message in passwword
        elif password_user != conform_user:
            messagebox.showerror("Information","Enter valid password")

        else:
            # for opening file i have created and write information in that file
            with open("Register.txt","a") as file:
                file.write("\n")
                file.write(firstname_user.lower())
                file.write("-----")
                file.write(lastname_user)
                file.write("-----")
                file.write(mobile_user)
                file.write("-----")
                file.write(username_user)
                file.write("-----")
                file.write(password_user)
                file.write("-----")
                file.write(gender_user)
                file.write("-----")
                file.write(day_user)
                file.write("/")
                file.write(month_user)
                file.write("/")
                file.write(year_user)
            #message for account made
            messagebox.showinfo("Account Info","Your account is created")
            #This will switch frame to login screen
            self.master.switch_frame(Login_Screen)

    # This function will keep username and password
    def taking_user_password(self):
        username_list=[]
        password_list=[]
        with open("Register.txt","r") as file:
            wholedocument=file.readlines()
            for line in wholedocument:
                making_list_of_info=line.split("-----")
                try:
                    username_list.append(making_list_of_info[3])
                    password_list.append(making_list_of_info[4])
                except:
                    pass
            return username_list,password_list

    # For reset written information
    def reset(self):
        self.firstname_entry.delete(0,tk.END)
        self.lastname_entry.delete(0,tk.END)
        self.mobile_entry.delete(0,tk.END)
        self.username_entry.delete(0,tk.END)
        self.password_entry.delete(0,tk.END)
        self.conform_password_entry.delete(0,tk.END)

    # Function for going to previous page
    def back(self):
        self.destroy()
        # This will switch frame for login pages
        self.master.switch_frame(Login_Screen)


call=Main()
call.mainloop()

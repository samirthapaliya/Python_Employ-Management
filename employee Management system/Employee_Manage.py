# importing tkinter modules
from tkinter import *
# This module is for combobox
from tkinter import ttk,messagebox
# This module is for file directory
import os

class File_App():
    # The bellow code will create a GUI window and adding some color and features on it
    def __init__(self,root):
        self.root=root
        self.root.title("Employee Management System")
        self.root.config(bg="#3E5C9A")
        self.root.geometry("1350x720+0+0")
        #  heading of the page
        Label(self.root,text="Employee Management System",font=("time new roman",35,"bold"),
                    bg="#3E5C9A",bd=10,relief=GROOVE,pady=10,fg="white").pack(fill=X)

#========================for making employee detail======================================================
        Employee_Frame=Frame(self.root,bd=10,relief=GROOVE,bg="azure")
        Employee_Frame.place(x=20,y=100,height=480)

        Label(Employee_Frame,text="Employee Detail",bg="azure",
                     font=("times new roman",30,"bold")).grid(row=0,column=0,columnspan=4,pady=10)
        # =========All Variable========================================================================================
        self.e_id = StringVar()
        self.name = StringVar()
        self.contact = StringVar()
        self.department = StringVar()
        self.country = StringVar()
        self.date = StringVar()
        self.code = StringVar()
        self.degree = StringVar()
        self.address = StringVar()
        self.salary = StringVar()
        self.gender = StringVar()
        self.payment = StringVar()

        # this will create a labels and some function is added so that it look good
        Label(Employee_Frame, text="Employee ID", bg="azure",
              font=("times new roman", 20, "bold")).grid(row=1, column=0, padx=20, sticky="W")
        Entry(Employee_Frame, bd=7, textvariable=self.e_id, relief=GROOVE, width=22,
              font=("arial", 15, "bold")).grid(row=1, column=1, padx=10, pady=10)
        #contact
        Label(Employee_Frame, text="Contact No.", bg="azure",
              font=("times new roman", 20, "bold")).grid(row=1, column=2, padx=20, sticky="W")
        Entry(Employee_Frame, bd=7, textvariable=self.contact, relief=GROOVE, width=22,
              font=("arial", 15, "bold")).grid(row=1, column=3, padx=10, pady=10)
        #fullname
        Label(Employee_Frame, text="Full Name", bg="azure",
              font=("times new roman", 20, "bold")).grid(row=2, column=0, padx=20, sticky="W")
        Entry(Employee_Frame, bd=7, relief=GROOVE, width=22, textvariable=self.name,
              font=("arial", 15, "bold")).grid(row=2, column=1, padx=10, pady=10)
        # age
        Label(Employee_Frame, text="Date of Birth", bg="azure",
              font=("times new roman", 20, "bold")).grid(row=2, column=2, padx=20, sticky="W")
        Entry(Employee_Frame, bd=7, relief=GROOVE, width=22, textvariable=self.date,
              font=("arial", 15, "bold")).grid(row=2, column=3, padx=10, pady=10)
        # department
        Label(Employee_Frame, text="Department", bg="azure",
              font=("times new roman", 20, "bold")).grid(row=3, column=0, padx=20, sticky="W")
        # entry for department
        departmentcombo = ttk.Combobox(Employee_Frame, textvariable=self.department, width=20,
                                       state="readonly", font=("arial", 15, "bold"))
        departmentcombo["value"] = ("Finance","IT", "Counseling", "Student",  "Teacher", "Security", "Maintenance",
                                    "Strategic Management", "Driver", "Canteen")
        departmentcombo.grid(row=3, column=1, padx=10, pady=10)

        # Department code
        Label(Employee_Frame, text="Department Code", bg="azure",
              font=("times new roman", 20, "bold")).grid(row=3, column=2, padx=20, sticky="W")
        Entry(Employee_Frame, bd=7, relief=GROOVE, width=22, textvariable=self.code,
              font=("arial", 15, "bold")).grid(row=3, column=3, padx=10, pady=10)
        # country
        Label(Employee_Frame, text="Country", bg="azure",
              font=("times new roman", 20, "bold")).grid(row=4, column=0, padx=20, sticky="W")
        Entry(Employee_Frame, bd=7, relief=GROOVE, width=22, textvariable=self.country,
              font=("arial", 15, "bold")).grid(row=4, column=1, padx=10, pady=10)
        # Qualification and drop down menu
        Label(Employee_Frame, text="Qualification", bg="azure",
              font=("times new roman", 20, "bold")).grid(row=4, column=2, padx=20, sticky="W")
        # This will make a columnbox
        degreecombo = ttk.Combobox(Employee_Frame, textvariable=self.degree, width=20, state="readonly",
                                   font=("arial", 15, "bold"))
        degreecombo["values"] = ("BSc.Computing", "BCA", "MCA", "BIT", "BHM", "BBA", "MBA")
        degreecombo.grid(row=4, column=3, padx=10, pady=10)
        # address
        Label(Employee_Frame, text="Address", bg="azure",
              font=("times new roman", 20, "bold")).grid(row=5, column=0, padx=20, sticky="W")
        Entry(Employee_Frame, bd=7, relief=GROOVE, width=22, textvariable=self.address,
              font=("arial", 15, "bold")).grid(row=5, column=1, padx=10, pady=10)
        # salary
        Label(Employee_Frame, text="Salary", bg="azure",
              font=("times new roman", 20, "bold")).grid(row=5, column=2, padx=20, sticky="W")
        Entry(Employee_Frame, bd=7, relief=GROOVE, width=22, textvariable=self.salary,
              font=("arial", 15, "bold")).grid(row=5, column=3, padx=10, pady=10)
        # gender
        Label(Employee_Frame, text="Gender", bg="azure",
              font=("times new roman", 20, "bold")).grid(row=6, column=0, padx=20, sticky="W")
        # columnbox for gender
        gendercombo = ttk.Combobox(Employee_Frame, textvariable=self.gender, width=20, state="readonly",
                                   font=("arial", 15, "bold"))
        gendercombo["values"] = ("Male", "Female", "Other")
        gendercombo.grid(row=6, column=1, padx=10, pady=10)
        # Payment method
        Label(Employee_Frame, text="Payment Method", bg="azure",
              font=("times new roman", 20, "bold")).grid(row=6, column=2, padx=20, sticky="W")
        # colunmbox for payment
        paymentcombo = ttk.Combobox(Employee_Frame, textvariable=self.payment, width=20, state="readonly",
                                    font=("arial", 15, "bold"))
        paymentcombo["values"] = ("Cash", "Credit Card", "Internet Banking")
        paymentcombo.grid(row=6, column=3, padx=10, pady=10)

#==================frame for buttons===================================================================
        btnFrame=Frame(self.root,bd=10,relief=GROOVE,bg="#3E5C9A")
        #This will set the position of frame where it should be written
        btnFrame.place(x=10,y=600)
        # for Save button
        Button(btnFrame,text="Save",font=("arial",16,"bold"),bg="#3E5C9A",fg="white",command=self.save_data,
                      bd=7,width=18).grid(row=0,column=0,padx=10,pady=10)
        # for Delete button
        Button(btnFrame, text="Delete", font=("arial", 16, "bold"),bg="#3E5C9A",command=self.delete,
                        fg="white",bd=7, width=18).grid(row=0, column=1, padx=10, pady=10)
        # for clear button
        Button(btnFrame, text="Clear", font=("arial", 15, "bold"),bg="#3E5C9A",command=self.clear,
                        fg="white",bd=7, width=18).grid(row=0, column=2, padx=10, pady=10)
        # for logout button
        Button(btnFrame, text="Logout", font=("arial", 15, "bold"),bg="#3E5C9A",command=self.logout,
                        fg="white",bd=7, width=18).grid(row=0, column=3, padx=10, pady=10)
        # for exit button
        Button(btnFrame, text="Exit", font=("arial", 15, "bold"),bg="red",command=self.exit_func,
                        fg="white",bd=7, width=18).grid(row=0, column=4, padx=10, pady=10)

#========================frame for Showing files======================================================
        File_Frame=Frame(self.root,bd=10,relief=GROOVE,bg="azure")
        #position
        File_Frame.place(x=1050,y=100,width=300,height=480)
        # header name
        Label(File_Frame,text="All Files",font=("arial",20,"bold"),bg="#3E5C9A",
                     fg="white",bd=4,relief=GROOVE).pack(side=TOP,fill=X),
        # left side vertical scroll bar
        scroll_y=Scrollbar(File_Frame,orient=VERTICAL)
        #list box and adding some function on it
        self.file_list=Listbox(File_Frame,yscrollcommand=scroll_y.set,bg="azure")
        #positio of scroll bar
        scroll_y.pack(side=RIGHT,fill=Y)
        #this will attach list bar and scroll bar
        scroll_y.config(command=self.file_list.yview)
        self.file_list.pack(fill=BOTH,expand=1)
        self.file_list.bind("<ButtonRelease-1>",self.get_data)
        self.show_files()

    def save_data(self):
        present = "no"
        #checking whether it is correct
        if self.e_id.get == "":
            messagebox.showerror("Error", "Employee ID must be Required!")
        else:
            f = os.listdir("Employee/")
            if len(f) > 0:
                for i in f:
                    # adding using(.) in saveing file
                    if i.split(".")[0] == self.e_id.get():
                        present = "yes"
                if present == "yes":
                    ask = messagebox.askyesno("Update", "File already present\n Do you really want to Update?")
                    if ask > 0:
                        self.save_file()
                        messagebox.showinfo("Update","Record has updated Successfully")
                        self.show_files()
                else:
                    self.save_file()
                    messagebox.showinfo("Saved", "saved Successfully")
                    self.show_files()
            else:
                self.save_file()
                messagebox.showinfo("Saved", "saved Successfully")
                self.show_files()


    def save_file(self):
        # directory for employ id
        f = open("Employee/" + str(self.e_id.get()) + ".txt", "w") # mode w=writable
        #wrriting all data in file
        f.write(
                str(self.e_id.get()) + "," +
                str(self.name.get()) + "," +
                str(self.department.get()) + "," +
                str(self.country.get()) + "," +
                str(self.address.get()) + "," +
                str(self.gender.get()) + "," +
                str(self.contact.get()) + "," +
                str(self.date.get()) + "," +
                str(self.code.get()) + "," +
                str(self.degree.get()) + "," +
                str(self.salary.get()) + "," +
                str(self.payment.get())
                )
        f.close()

    def show_files(self):
        # This will give path using os module
        files = os.listdir("Employee/")
        #This will delete a duplicate data
        self.file_list.delete(0, END)
        if len(files)>0:
            for i in files:
                self.file_list.insert(END,i)

    # For fetching data
    def get_data(self,ev):
        get_cursor=self.file_list.curselection()
        f1=open("Employee/"+self.file_list.get(get_cursor))
        value=[]
        for f in f1:
            value=f.split(",")
        # For setting position
        self.e_id.set(value[0])
        self.name.set(value[1])
        self.department.set(value[2])
        self.country.set(value[3])
        self.address.set(value[4])
        self.gender.set(value[5])
        self.contact.set(value[6])
        self.date.set(value[7])
        self.code.set(value[8])
        self.degree.set(value[9])
        self.salary.set(value[10])
        self.payment.set(value[11])

    def clear(self):
        self.e_id.set("")
        self.name.set("")
        self.department.set("")
        self.country.set("")
        self.address.set("")
        self.gender.set("")
        self.contact.set("")
        self.date.set("")
        self.code.set("")
        self.degree.set("")
        self.salary.set("")
        self.payment.set("")
    def delete(self):
        present="no"
        #using if else checking whether it is correct or not
        if self.e_id.get=="":
            messagebox.showerror("Error","Employee ID must be Required!")
        else:
            f=os.listdir("Employee/")
            if len(f)>0:
                for i in f:
                    # saved files are saved as 101.txt so spiting with (".") operator
                    if i.split(".")[0] == self.e_id.get():
                        present="yes"
                if present=="yes":
                    ask=messagebox.askyesno("Delete","Do you really want to Delete?")
                    #Checking whether the value is present or not
                    if ask>0:
                        os.remove("Employee/"+self.e_id.get()+".txt")
                        messagebox.showinfo("Success","Deleted Successfully")
                        self.show_files() #For showing file
                else:
                    messagebox.showerror("Error","File not found")

    def exit_func(self):
        ask = messagebox.askyesno("Exit", "Do you really want to Exit?")
        # final checking value is present or not
        if ask > 0:
            self.root.destroy()

    def logout(self):
        ask=messagebox.askyesno("Logout","Do you really want to Logout?")
        if ask>0:
            self.root.destroy()
            #for changing directory
            import User_Managment

root=Tk()
ob=File_App(root)
root.mainloop()
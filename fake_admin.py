#fake admin

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import *
import mysql.connector as sq


def connection():
    conn = sq.connect(
        host='localhost',
        user='root', 
        password='adishree',
        db='world',
    )
    return conn

def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)

    for array in read():
        my_tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")

    my_tree.tag_configure('orow', background='white', font=('Times New Roman', 12))
    my_tree.grid(row=8, column=0, columnspan=5, rowspan=11, padx=10, pady=20)

root = Tk() 
root.geometry('900x600+50+50')
root.configure(bg="black")
root.title("STUDENT PROFILE MANAGER")
my_tree = ttk.Treeview(root)

ph1 = tk.StringVar()
ph2 = tk.StringVar()
ph3 = tk.StringVar()
ph4 = tk.StringVar()
ph5 = tk.StringVar()
ph6 = tk.StringVar()


def setph(word,num):
    if num ==1:
        ph1.set(word)
    if num ==2:
        ph2.set(word)
    if num ==3:
        ph3.set(word)
    if num ==4:
        ph4.set(word)
    if num ==5:
        ph5.set(word)
    if num ==6:
        ph6.set(word)

def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM profile")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results

def add():
    profileid = str(profileidEntry.get())
    name = str(nameEntry.get())
    email = str(emailEntry.get())
    address = str(addressEntry.get())
    phone = str(phoneEntry.get())
    Class = str(classEntry.get())
    decision = messagebox.askquestion("Add", "Add entered data?")
    if (profileid == "" or profileid == " ") or (name == "" or name == " ") or (email == "" or email == " ") or (address == "" or address == " ") or (phone == "" or phone == " ") or (Class=="" or Class==" "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    elif len(phone)!=10:
        messagebox.showinfo("Error", "Mobile Number must be of 10 digits")
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO profile VALUES ('"+profileid+"','"+name+"','"+email+"','"+address+"','"+phone+"','"+Class+"') ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Profile ID already exist")
            return

    refreshTable()
    

def reset():
    decision = messagebox.askquestion("Warning!!", "Delete all data?")
    if decision != "yes":
        return 
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM profile")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Sorry an error occured")
            return

        refreshTable()

def delete():
    decision = messagebox.askquestion("Warning!!", "Delete the selected data?")
    if decision != "yes":
        return 
    else:
        selected_item = my_tree.selection()[0]
        deleteData = str(my_tree.item(selected_item)['values'][0])
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM profile WHERE Profile_ID='"+str(deleteData)+"'")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Sorry an error occured")
            return

        refreshTable()

def select():
    try:
        selected_item = my_tree.selection()[0]
        profileid = str(my_tree.item(selected_item)['values'][0])
        name = str(my_tree.item(selected_item)['values'][1])
        email = str(my_tree.item(selected_item)['values'][2])
        address = str(my_tree.item(selected_item)['values'][3])
        phone = str(my_tree.item(selected_item)['values'][4])
        Class = str(my_tree.item(selected_item)['values'][5])

        setph(profileid,1)
        setph(name,2)
        setph(email,3)
        setph(address,4)
        setph(phone,5)
        setph(Class,6)
        
    except:
        messagebox.showinfo("Error", "Please select a data row")

def search():
    profileid = str(profileidEntry.get())
    name = str(nameEntry.get())
    email = str(emailEntry.get())
    address = str(addressEntry.get())
    phone = str(phoneEntry.get())
    Class = str(classEntry.get())

    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM profile WHERE Profile_ID='"+
    profileid+"' or NAME='"+
    name+"' or Email_Id='"+
    email+"' or ADDRESS='"+
    address+"' or PHONE='"+
    phone+"' or CLASS='"+
    Class+"' ")
    
    try:
        result = cursor.fetchall()

        for num in range(0,5):
            setph(result[0][num],(num+1))

        conn.commit()
        conn.close()
    except:
        messagebox.showinfo("Error", "No data found")

def update():
    decision = messagebox.askquestion("UPDATE", "Update selected data?")
    selectedprofileid = ""

    try:
        selected_item = my_tree.selection()[0]
        selectedprofileid = str(my_tree.item(selected_item)['values'][0])
    except:
        messagebox.showinfo("Error", "Please select a data row")

    profileid = str(profileidEntry.get())
    name = str(nameEntry.get())
    email = str(emailEntry.get())
    address = str(addressEntry.get())
    phone = str(phoneEntry.get())
    Class = str(classEntry.get())

    if (profileid == "" or profileid == " ") or (name == "" or name == " ") or (email == "" or email == " ") or (address == "" or address == " ") or (phone == "" or phone == " ") or (Class=="" or Class==" "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE profile SET Profile_ID='"+
            profileid+"', NAME='"+
            name+"', Email_Id='"+
            email+"', ADDRESS='"+
            address+"', PHONE='"+
            phone+"', CLASS='"+
            Class+"' WHERE Profile_ID='"+
            selectedprofileid+"' ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Profile ID already exist")
            return

    refreshTable()

def logout():
    root.destroy()
    import Fake_login
    
label = Label(root, text="STUDENT MANAGEMENT SYSTEM", font=('Algerian', 25),bg="white")
label.grid(row=0, column=0, columnspan=8, rowspan=2, padx=10, pady=10)

profileidLabel = Label(root, text="PROFILE ID", font=('Arial', 15),bg="white")
nameLabel = Label(root, text="NAME", font=('Arial', 15),bg="white")
emailLabel = Label(root, text="EMAIL", font=('Arial', 15),bg="white")
addressLabel = Label(root, text="ADDRESS", font=('Arial', 15),bg="white")
phoneLabel = Label(root, text="PHONE", font=('Arial', 15),bg="white")
classLabel = Label(root, text="CLASS", font=('Arial', 15),bg="white")

profileidLabel.grid(row=2, column=0, columnspan=1, padx=12, pady=2)
nameLabel.grid(row=3, column=0, columnspan=1, padx=12, pady=2)
emailLabel.grid(row=4, column=0, columnspan=1, padx=12, pady=2)
addressLabel.grid(row=5, column=0, columnspan=1, padx=12, pady=2)
phoneLabel.grid(row=6, column=0, columnspan=1, padx=12, pady=2)
classLabel.grid(row=7, column=0, columnspan=1, padx=12, pady=2)

profileidEntry = Entry(root, width=55, bd=3, font=('Arial', 15), textvariable = ph1)
nameEntry = Entry(root, width=55, bd=3, font=('Arial', 15), textvariable = ph2)
emailEntry = Entry(root, width=55, bd=3, font=('Arial', 15), textvariable = ph3)
addressEntry = Entry(root, width=55, bd=3, font=('Arial', 15), textvariable = ph4)
phoneEntry = Entry(root, width=55, bd=3, font=('Arial', 15), textvariable = ph5)
classEntry = Entry(root, width=55, bd=3, font=('Arial', 15), textvariable = ph6)

profileidEntry.grid(row=2, column=1, columnspan=1, padx=1, pady=0)
nameEntry.grid(row=3, column=1, columnspan=1, padx=1, pady=0)
emailEntry.grid(row=4, column=1, columnspan=1, padx=2, pady=0)
addressEntry.grid(row=5, column=1, columnspan=1, padx=3, pady=0)
phoneEntry.grid(row=6, column=1, columnspan=1, padx=3, pady=0)
classEntry.grid(row=7, column=1, columnspan=1, padx=3, pady=0)

addBtn = Button(
    root, text="Add", padx=25, pady=10, width=5,
    bd=5, font=('lucida', 13), bg="orange", command=add)
updateBtn = Button(
    root, text="Update", padx=25, pady=10, width=5,
    bd=5, font=('lucida', 13), bg="blue", command=update)
deleteBtn = Button(
    root, text="Delete", padx=25, pady=10, width=5,
    bd=5, font=('lucida', 13), bg="green", command=delete)
searchBtn = Button(
    root, text="Search", padx=25, pady=10, width=5,
    bd=5, font=('lucida', 13), bg="yellow", command=search)
resetBtn = Button(
    root, text="Reset All", padx=25, pady=10, width=5,
    bd=5, font=('lucida', 13), bg="orange", command=reset)
selectBtn = Button(
    root, text="Select", padx=25, pady=10, width=5,
    bd=5, font=('lucida', 13), bg="white", command=select)
logoutBtn = Button(
    root, text="Log Out", padx=25, pady=10, width=5,
    bd=5, font=('lucida', 13), bg="deep pink", command=logout)

addBtn.grid(row=0, column=5, columnspan=1, rowspan=3)
updateBtn.grid(row=3, column=5, columnspan=1, rowspan=1)
deleteBtn.grid(row=4, column=5, columnspan=1, rowspan=1)
searchBtn.grid(row=5, column=5, columnspan=1, rowspan=1)
resetBtn.grid(row=6, column=5, columnspan=1, rowspan=1)
selectBtn.grid(row=7, column=5, columnspan=1, rowspan=2)
logoutBtn.grid(row=9, column=5, columnspan=1, rowspan=1)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial Bold', 15))

scrollbary=Scrollbar(root,orient=VERTICAL)
scrollbary.configure(command=my_tree.yview)
my_tree.configure(yscrollcommand=scrollbary.set)
scrollbary.place(relx=0.8524,rely=0.68,width=22,height=176)
my_tree.configure(selectmode="extended")


my_tree['columns'] = ("PROFILE ID","NAME","EMAIL ID","ADDRESS","PHONE","CLASS")
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("PROFILE ID", anchor=CENTER, width=170)
my_tree.column("NAME", anchor=CENTER, width=150)
my_tree.column("EMAIL ID", anchor=CENTER, width=150)
my_tree.column("ADDRESS", anchor=CENTER, width=165)
my_tree.column("PHONE", anchor=CENTER, width=150)
my_tree.column("CLASS", anchor=CENTER, width=160)

my_tree.heading("PROFILE ID", text="PROFILE ID", anchor=CENTER)
my_tree.heading("NAME", text="NAME", anchor=CENTER)
my_tree.heading("EMAIL ID", text="EMAIL ID", anchor=CENTER)
my_tree.heading("ADDRESS", text="ADDRESS", anchor=CENTER)
my_tree.heading("PHONE", text="PHONE", anchor=CENTER)
my_tree.heading("CLASS", text="CLASS", anchor=CENTER)

refreshTable()

root.mainloop()



from tkinter import *
from tkinter import ttk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from PIL import Image,ImageTk
from subprocess import call
import mysql.connector as sq

root = Tk()
root.configure(background="black")
root.title('THREE LEVELS')
label1 = Label(root, text="CREDIT MANAGEMENT SYSTEM", font=('Bookman Old Style', 30),bg="white")
label1.grid(row=0, column=0, columnspan=8, rowspan=2, padx=200, pady=55)
    
def admin():

    import Fake_login_admin

adminbutton1 = Button(root, text='ADMIN', font=('Bookman Old Style', 25, 'bold'), fg='white', bg='blue',
                      activebackground='orange', activeforeground='white',command=admin)
adminbutton1.place(x=200, y=200)

def students():
    
    import Fake_login_student

studentbutton2 = Button(root, text='STUDENTS', font=('Bookman Old Style', 25, 'bold'), fg='white', bg='blue',
                      activebackground='white', activeforeground='red',command=students)
studentbutton2.place(x=380, y=200)

def teachers():
    
    import Fake_login_teacher

teacherbutton3 = Button(root, text='TEACHERS', font=('Bookman Old Style', 25, 'bold'), fg='white', bg='blue',
                      activebackground='green', activeforeground='white',command=teachers)
teacherbutton3.place(x=630, y=200)

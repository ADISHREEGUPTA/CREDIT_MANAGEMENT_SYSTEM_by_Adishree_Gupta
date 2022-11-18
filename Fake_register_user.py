from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from PIL import Image,ImageTk
import mysql.connector as sq

def login_window():
    import Fake_login_general
    
def clear():
    
    entrycontact.delete(0, END)
    entrypassword.delete(0, END)
    entryconfirmpassword.delete(0, END)
    entryusername.delete(0, END)
    entryfirstname.delete(0, END)
    entrylastname.delete(0, END)
    entryanswer.delete(0, END)
    check.set(0)
    
def register():
    if entryfirstname.get() == '' or entrylastname.get() == '' or entrycontact.get() == '' or entryusername.get() == '' or \
           entrypassword.get() == '' or entryconfirmpassword.get() == '' or entryanswer.get() == '':
        showerror('Error', "All Fields Are Required", parent=root)
    elif len(entrycontact.get()) != 10:
        showerror('Error', "Phone number must be of 10 digits", parent=root)
        
    elif len(entrypassword.get()) != 8:
        showerror('Error', "Password must be alphanumeric and must have 8 characters", parent=root)

    elif entrypassword.get() != entryconfirmpassword.get():
        showerror('Error', "Password Mismatch", parent=root)

    elif check.get() == 0:
        showerror('Error', "Please Agree To Our Terms & Conditions", parent=root)

    else:
        try:
            con = sq.connect(host='localhost',user='root',password='adishree', database='credit_management_system')
            cur = con.cursor()
            code='insert into user(f_name,l_name,contact,username,date_of_birth,password) values(%s,%s,%s,%s,%s,%s)'
            values=(entryfirstname.get(), entrylastname.get(),entrycontact.get(),entryusername.get(),entryanswer.get(), entrypassword.get(),)
            cur.execute(code,values)
            con.commit()
            con.close()
            showinfo('Success', "Registration Successful", parent=root)
            clear()

        except Exception as e:
            showerror('Error', f"Error due to: {e}", parent=root)


root = Tk()
root.configure(bg="black")
root.title('USER REGISTRATION')

titleLabel = Label(root, text='Registration Form', font=('Bookman Old Style', 40, 'bold '),bg='black',
                   fg='white', )
titleLabel.place(x=250, y=50)

firstnameLabel = Label(root, text='First Name', font=('Bookman Old Style', 16, 'bold'), bg='black',
                       fg='white', )
firstnameLabel.place(x=250, y=140)
entryfirstname = Entry(root, font=('Bookman Old Style', 16), bg='white')
entryfirstname.place(x=200, y=175, width=250, height=24)

lastnameLabel = Label(root, text='Last Name', font=('Bookman Old Style', 16, 'bold'), bg='black',
                      fg='white', )
lastnameLabel.place(x=600, y=140)
entrylastname = Entry(root, font=('Bookman Old Style', 16), bg='white')
entrylastname.place(x=550, y=175, width=250,height=24)

contactLabel = Label(root, text='Contact Number', font=('Bookman Old Style', 16, 'bold'), bg='black',
                     fg='white', )
contactLabel.place(x=225, y=230)
entrycontact = Entry(root, font=('Bookman Old Style', 16), bg='white')
entrycontact.place(x=200, y=265, width=250,height=24)

UsernameLabel = Label(root, text='Username', font=('Bookman Old Style', 16, 'bold'), bg='black',
                     fg='white', )
UsernameLabel.place(x=600, y=230)
entryusername = Entry(root, font=('Bookman Old Style', 16), bg='white')
entryusername.place(x=550, y=265, width=250,height=24)

DOBLabel = Label(root, text='Date of Birth', font=('Bookman Old Style', 20, 'bold'), bg='black',
                      fg='white', )
DOBLabel.place(x=225, y=330)

entryanswer = Entry(root, font=('Bookman Old Style', 16), bg='white')
entryanswer.place(x=550, y=330, width=250,height=24)

passwordLabel = Label(root, text='Password', font=('Bookman Old Style', 16, 'bold'), bg='black',
                      fg='white', )
passwordLabel.place(x=250, y=390)
entrypassword = Entry(root,show="*", font=('Bookman Old Style', 16), bg='white')
entrypassword.place(x=200, y=430, width=250,height=24)

confirmpasswordLabel = Label(root, text='Confirm Password', font=('Bookman Old Style', 16, 'bold'),
                             bg='black',
                             fg='white', )
confirmpasswordLabel.place(x=575, y=390)
entryconfirmpassword = Entry(root,show="*", font=('Bookman Old Style', 16), bg='white')
entryconfirmpassword.place(x=550, y=430, width=250,height=24)

check = IntVar()
checkButton = Checkbutton(root, text='I Agree All The Terms & Conditions', variable=check, onvalue=1,
                          offvalue=0, font=('times new roman', 10,), bg='white')
checkButton.place(x=215, y=490)

registerbutton = Button(root,text="Register",font=('Bookman Old Style', 18, 'bold'), bd=0, cursor='hand2', fg='white', bg='navy blue', activebackground='white'
                        , activeforeground='white', command=register)
registerbutton.place(x=680, y=480)

loginbutton1 = Button(root,text="Login", font=('Bookman Old Style', 18, 'bold',), bd=0, cursor='hand2', fg='white', bg='navy blue', activebackground='gold',
                      activeforeground='gold', command=login_window)
loginbutton1.place(x=550, y=480)

root.mainloop()


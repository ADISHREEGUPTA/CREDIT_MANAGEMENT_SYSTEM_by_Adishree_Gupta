from tkinter import *
from tkinter import ttk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from PIL import Image,ImageTk
from subprocess import call
import mysql.connector as sq

def register_window():
    import Fake_register_user
def interface():
    import three_levels
    
def signin():
    if userentry.get() == '' or passentry.get() == '':
        showerror('Error', 'All Fields Are Required')

    else:
        try:
            con = sq.connect(host='localhost',user='root',password='adishree', database='credit_management_system')
            cur = con.cursor()
            cur.execute('select * from user where username=%s and password=%s', (userentry.get(), passentry.get()))
            row = cur.fetchone()
            if row == None:
                showerror('error', 'Invalid username or Password')
                root.destroy()
            else:
                showinfo('Authenticated', 'Welcome')
                interface()
            con.close()
        except Exception as e:
            showerror('Error', f"Error due to: {e}", parent=root)
            
def forgot_password():
    
    def authentication():
        
        if user_entry.get()==" " or DOB_entry.get()==" " or newpass_entry==" ":
            showerror('Error', 'All Fields Are Required',parent=window)
        else:
            con = sq.connect(host='localhost',user='root',password='adishree', database='credit_management_system')
            cur = con.cursor()
            query='select * from user where username=%s and date_of_birth=%s'
            cur.execute(query,(user_entry.get(),DOB_entry.get()))
            row=cur.fetchone()
            if row==None:
                message.showerror('Error','Incorrect username and date of birth',parent=window)
            else:
                query='update user set password=%s where username=%s and date_of_birth=%s'
                cur.execute(query,(newpass_entry.get(),user_entry.get(),DOB_entry.get()))
                con.commit()
                con.close()
                showinfo('Success','Password is reset,please login with new password',parent=window)
                window.destroy()
                
    window=Toplevel()
    window.title("Forgot password")
    
    window.configure(bg="black")

    heading_label = Label(window,text="Password Manager",font=('Algerian','50' , 'bold'),bg='black',fg='white')
    heading_label.place(x=200,y=60)

    userlabel=Label(window,text=" Username   ",font=('Algerian','20' , 'bold'),bg='black',fg='white')
    userlabel.place(x=200,y=200)

    user_entry=Entry(window,width=25,fg='black',font=('Algerian','20','italic'),bd=0)
    user_entry.place(x=520,y=200)

    DOBlabel=Label(window,text="Date of Birth",font=('Algerian','20' , 'bold'),bg='black',fg='white')
    DOBlabel.place(x=200,y=250)

    DOB_entry=Entry(window,width=25,fg='black',font=('Algerian','20','italic'),bd=0)
    DOB_entry.place(x=520,y=250)

    newpasslabel=Label(window,text="New Password",font=('Algerian','20' , 'bold'),bg='black',fg='white')
    newpasslabel.place(x=200,y=300)

    newpass_entry=Entry(window,width=25,fg='black',font=('Algerian','20','italic'),bd=0)
    newpass_entry.place(x=520,y=300)

    resetbutton = Button(window,text="RESET", font=('Bookman Old Style', 28, 'bold',), bd=0, cursor='hand2', fg='white', bg='red', activebackground='gold',
                      activeforeground='gold', command=authentication)
    resetbutton.place(x=410, y=380)

    window.mainloop()

root = Tk()
root.configure(background="black")
root.title('USER LOGIN')

frame = Frame(root, bg='white', width=560, height=320)
frame.place(x=50, y=140)

label = Label(root, text="USER LOGIN", font=('Algerian', 25),bg="white")
label.grid(row=0, column=0, columnspan=8, rowspan=2, padx=200, pady=105)

mailLabel = Label(frame, text='Username', font=('arial', 22, 'bold'), bg='white', fg='black')
mailLabel.place(x=200, y=32)
userentry = Entry(frame, font=('arial', 22,), bg='white', fg='black')
userentry.place(x=110, y=70)

passLabel = Label(frame, text='Password', font=('arial', 22, 'bold'), bg='white', fg='black')
passLabel.place(x=200, y=120)
passentry = Entry(frame,show="*",font=('arial', 22,), bg='white', fg='black')
passentry.place(x=110, y=160)

regbutton = Button(frame,text="Register New Account?", bd=0, cursor='hand2', bg='gold', activebackground='gold',
                      activeforeground='gold', command=register_window)
regbutton.place(x=300, y=230)

forgotbutton = Button(frame,text="Forgot Password", bd=0, cursor='hand2', bg='gold', activebackground='gold',
                      activeforeground='gold', command=forgot_password)
forgotbutton.place(x=125, y=230)

loginbutton2 = Button(frame, text='Login', font=('arial', 18, 'bold'), fg='white', bg='gray20', cursor='hand2',
                      activebackground='gray20', activeforeground='white', command=signin)
loginbutton2.place(x=230, y=280)

root.mainloop()

from tkinter import*
from PIL import Image,ImageTk
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

root=Tk()
        
        #basic window
root.title("CREDIT BOOSTER")        
        #Background Image

root.geometry('900x600+50+50')
root.configure(bg="black")

        #Regd Frame
frame1=Frame(root,bg="white")
frame1.place(x=70,y=30,width=960,height=500)

        #Elements in frame

title=Label(frame1,text="Questionnaire" , font=("time new roman",20,"bold"),bg= "white" ,fg ="green").place(x=360,y=10)
        # self.R1 = Radiobutton(frame1,text="Radio",value=2)
        # self.R1.place(x=50,y=100)
       
name=Label(frame1,text="What is your full name ",font=("time new roman",10,"bold"),bg= "white" ,fg ="gray").place(x=30,y=70)
entryname = Entry(frame1, font=('Bookman Old Style', 16), bg='white')
entryname.place(x=700, y=70, width=250, height=24)
que1=Label(frame1,text="Was your overall grade in the terminal examinations an A?" , font=("time new roman",10,"bold"),bg= "white" ,fg ="gray").place(x=30,y=100)
que1 = ttk.Combobox(frame1,font=("time new roman",10),state = 'readonly',justify=CENTER)
que1['values'] = ("Select","yes","no")
que1.place(x=700,y=100,width=230)
que1.current(0)
que2=Label(frame1,text="Was your overall grade in the terminal examinations an B?" , font=("time new roman",10,"bold"),bg= "white" ,fg ="gray").place(x=30,y=130)
que2 = ttk.Combobox(frame1,font=("time new roman",10),state = 'readonly',justify=CENTER)
que2['values'] = ("Select","yes","no")
que2.place(x=700,y=130,width=230)
que2.current(0)
que3=Label(frame1,text="Did you win the first prize in any interhouse sports event?" , font=("time new roman",10,"bold"),bg= "white" ,fg ="gray").place(x=30,y=160)
que3 = ttk.Combobox(frame1,font=("time new roman",10),state = 'readonly',justify=CENTER)
que3['values'] = ("Select","yes","no")
que3.place(x=700,y=160,width=230)
que3.current(0)
que4=Label(frame1,text="Did you win the first prize in any other  interhouse co-curricular activity?" , font=("time new roman",10,"bold"),bg= "white" ,fg ="gray").place(x=30,y=190)
que4 = ttk.Combobox(frame1,font=("time new roman",10),state = 'readonly',justify=CENTER)
que4['values'] = ("Select","yes","no")
que4.place(x=700,y=190,width=230)
que4.current(0)
que5=Label(frame1,text="Did you win the first prize in any interschool sports event?" , font=("time new roman",10,"bold"),bg= "white" ,fg ="gray").place(x=30,y=220)
que5 = ttk.Combobox(frame1,font=("time new roman",10),state = 'readonly',justify=CENTER)
que5['values'] = ("Select","yes","no")
que5.place(x=700,y=220,width=230)
que5.current(0)
que6=Label(frame1,text="Did you win the second prize in any interschool sports event?" , font=("time new roman",10,"bold"),bg= "white" ,fg ="gray").place(x=30,y=250)
que6 = ttk.Combobox(frame1,font=("time new roman",10),state = 'readonly',justify=CENTER)
que6['values'] = ("Select","yes","no")
que6.place(x=700,y=250,width=230)
que6.current(0)
que7=Label(frame1,text="Did you win the first prize in any other interschool co-curricular activity(art,singing,dance)?" , font=("time new roman",10,"bold"),bg= "white" ,fg ="gray").place(x=30,y=280)
que7 = ttk.Combobox(frame1,font=("time new roman",10),state = 'readonly',justify=CENTER)
que7['values'] = ("Select","yes","no")
que7.place(x=700,y=280,width=230)
que7.current(0)
que8=Label(frame1,text="Did you win the second prize in any other interhouse co-curricular activity(art,singing,dance) ?" , font=("time new roman",10,"bold"),bg= "white" ,fg ="gray").place(x=30,y=310)
que8 = ttk.Combobox(frame1,font=("time new roman",10),state = 'readonly',justify=CENTER)
que8['values'] = ("Select","yes","no")
que8.place(x=700,y=310,width=230)
que8.current(0)
que9=Label(frame1,text="Did you participate in any state / district / national level competitions?" , font=("time new roman",10,"bold"),bg= "white" ,fg ="gray").place(x=30,y=340)
que9 = ttk.Combobox(frame1,font=("time new roman",10),state = 'readonly',justify=CENTER)
que9['values'] = ("Select","yes","no")
que9.place(x=700,y=340,width=230)
que9.current(0)    
que10=Label(frame1,text="Did you win any prizes in any state / district / national level competitions?" , font=("time new roman",10,"bold"),bg= "white" ,fg ="gray").place(x=30,y=370)
que10 = ttk.Combobox(frame1,font=("time new roman",10),state = 'readonly',justify=CENTER)
que10['values'] = ("Select","yes","no")
que10.place(x=700,y=370,width=230)
que10.current(0)
que11=Label(frame1,text="Have you done any volunteer/charity work?" , font=("time new roman",10,"bold"),bg= "white" ,fg ="gray").place(x=30,y=400)
que11 = ttk.Combobox(frame1,font=("time new roman",10),state = 'readonly',justify=CENTER)
que11['values'] = ("Select","yes","no")
que11.place(x=700,y=400,width=230)
que11.current(0)
def submit_ans():
    
    result=0
    if que1.get() =="yes":
       result+=100
    if que2.get() =="yes":
       result+=80
    if que3.get() =="yes":
       result+=50
    if que4.get() =="yes":
       result+=50
    if que5.get() =="yes":
       result+=80
    if que6.get() =="yes":
       result+=50
    if que7.get() =="yes":
       result+=80
    if que8.get() =="yes":
       result+=50
    if que9.get() =="yes":
       result+=80
    if que10.get() =="yes":
       result+=100
    if que11.get() =="yes":
       result+=150
    messagebox.showinfo("Bonus",str(result),parent=root)

    try:
            con = sq.connect(host='localhost',user='root',password='adishree', database='world')
            cur = con.cursor()
            code='insert into student_12_credits(name,credits) values(%s,%s)'
            values=(entryname.get(),str(result),)
            cur.execute(code,values)
            con.commit()
            con.close()
            showinfo('Success', "Submitted Successfully", parent=root)

    except Exception as e:
            showerror('Error', f"Error due to: {e}", parent=root)
    
submit=Button(frame1,text ="Submit",font=("time new roman",15),bd=0,cursor="hand2",command=submit_ans).place(x=30,y=440)


root.mainloop()

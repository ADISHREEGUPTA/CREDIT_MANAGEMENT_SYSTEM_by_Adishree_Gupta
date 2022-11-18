import mysql.connector as sq
def connection():
    conn = sq.connect(
        host='localhost',
        user='root', 
        password='adishree',
        db='world',
    )
    return conn
conn = connection()
cursor = conn.cursor()
cursor.execute("select r.name as NAME,r.age as AGE,r.class as CLASS,k.credits as CREDITS from class_12_details r, student_12_credits k where r.name=k.name group by class order by credits")
results = cursor.fetchall()
conn.commit()
import tkinter  as tk 
from tkinter import *
from PIL import Image,ImageTk
my_w = tk.Tk()
my_w.geometry('900x600+50+50')
my_w.configure(bg="black")
my_w.geometry("400x250") 
i=0 # row value inside the loop 
for student in results: 
    for j in range(len(student)):
        e = Entry(my_w, width=30, fg='blue') 
        e.grid(row=i, column=j) 
        e.insert(END, student[j])
    i=i+1
def save():
    f=open("C:\\Users\\eaningu\\OneDrive - Ericsson\\Desktop\\STAR\\student_12.txt","r+")
    for row in results:
        f.write(str(row))
savebutton=Button(my_w,text="SAVE",font=("ALGERIAN",20,"bold"),bg="blue",fg="white",command=save).place(x=400,y=400)
my_w.mainloop()

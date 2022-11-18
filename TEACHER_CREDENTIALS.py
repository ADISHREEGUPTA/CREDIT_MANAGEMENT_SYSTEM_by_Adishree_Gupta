from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from PIL import Image,ImageTk
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
root.configure(bg="black")
root.title('TEACHER CREDENTIALS')

titleLabel = Label(root, text='TEACHER CREDENTIALS', font=('Bookman Old Style', 40, 'bold '),bg='black',
                   fg='white', )
titleLabel.place(x=200, y=50)

nameLabel = Label(root, text='NAME', font=('Bookman Old Style', 16, 'bold'), bg='black',
                       fg='white', )
nameLabel.place(x=200, y=180)
entryname = Entry(root, font=('Bookman Old Style', 16), bg='white')
entryname.place(x=400, y=180, width=250, height=24)

def class9():
    import class_9_data

def class10():
    import class_10_data

def class11():
    import class_11_data

def class12():
    import class_12_data

class9button = Button(root,text="CLASS 9",font=('Bookman Old Style', 18, 'bold'), bd=0, cursor='hand2', fg='white', bg='navy blue', activebackground='white'
                        , activeforeground='white', command=class9)
class9button.place(x=200, y=300)
class10button = Button(root,text="CLASS 10",font=('Bookman Old Style', 18, 'bold'), bd=0, cursor='hand2', fg='white', bg='navy blue', activebackground='white'
                        , activeforeground='white', command=class10)
class10button.place(x=400, y=300)
class11button = Button(root,text="CLASS 11",font=('Bookman Old Style', 18, 'bold'), bd=0, cursor='hand2', fg='white', bg='navy blue', activebackground='white'
                        , activeforeground='white', command=class11)
class11button.place(x=200, y=400)
class12button = Button(root,text="CLASS 12",font=('Bookman Old Style', 18, 'bold'), bd=0, cursor='hand2', fg='white', bg='navy blue', activebackground='white'
                        , activeforeground='white', command=class12)
class12button.place(x=400, y=400)








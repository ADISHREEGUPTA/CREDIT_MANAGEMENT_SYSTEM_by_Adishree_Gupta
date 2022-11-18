from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from PIL import Image,ImageTk

root = Tk()
image = Image.open(r"C:\Users\eaningu\Anaconda3\pkgs\pillow-8.4.0-py39hd45dc43_0\Lib\site-packages\PIL\book.jpg")  
render=ImageTk.PhotoImage(image)
root.geometry('850x1050+0+10')
lbl=Label(root,image=render)
lbl.place(x=0,y=0)
root.title('STUDENT CREDENTIALS')

def CLASS_9():
    root.destroy()
    import CREDIT_BOOSTER
    
def CLASS_10():
    root.destroy()
    import CREDIT_BOOSTER

def CLASS_11():
    root.destroy()
    import CREDIT_BOOSTER

def CLASS_12():
    root.destroy()
    import CREDIT_BOOSTER

titleLabel = Label(root, text='STUDENT CREDENTIALS', font=('Bookman Old Style', 40, 'bold '),bg='white',
                   fg='navy blue' )
titleLabel.place(x=50, y=50)
nameLabel = Label(root, text='SELECT YOUR CLASS', font=('Bookman Old Style', 40, 'bold'), bg='white',
                       fg='gray20', )
nameLabel.place(x=50, y=190)

class9=Button(root,text="CLASS 9",font=('Bookman Old Style', 30, 'bold'), bd=0, cursor='hand2', fg='white', bg='navy blue', activebackground='white'
                        , activeforeground='white', command=CLASS_9)
class9.place(x=50, y=300)
class10=Button(root,text="CLASS 10",font=('Bookman Old Style', 30, 'bold'), bd=0, cursor='hand2', fg='white', bg='navy blue', activebackground='white'
                        , activeforeground='white', command=CLASS_10)
class10.place(x=50, y=400)
class11=Button(root,text="CLASS 11",font=('Bookman Old Style', 30, 'bold'), bd=0, cursor='hand2', fg='white', bg='navy blue', activebackground='white'
                        , activeforeground='white', command=CLASS_11)
class11.place(x=400, y=300)
class12=Button(root,text="CLASS 12",font=('Bookman Old Style', 30, 'bold'), bd=0, cursor='hand2', fg='white', bg='navy blue', activebackground='white'
                        , activeforeground='white', command=CLASS_12)
class12.place(x=400, y=400)

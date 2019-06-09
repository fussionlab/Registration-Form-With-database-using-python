from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()
root.geometry('500x500')
root.title("Registration Form")


Fullname=StringVar()
Email=StringVar()
var = IntVar()
c=StringVar()
var1= IntVar()

def reset():
	entry_1.delete(0,END)
	entry_2.delete(0,END)
	rb_1.deselect()
	rb_2.deselect()
	ch_1.deselect()
	ch_2.deselect()
	c.set("Select the Contry")
	label_5 = Label(root, text= " Record inserted successfully table",font=("bold", 14),fg="green")
	label_5.place(x=90,y=400)

def database():
   name1=Fullname.get()
   email=Email.get()
   gender=var.get()
   country=c.get()
   prog=var1.get()
   conn = sqlite3.connect('Form.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,Email TEXT,Gender TEXT,country TEXT,Programming TEXT)')
   cursor.execute('INSERT INTO Student (FullName,Email,Gender,country,Programming) VALUES(?,?,?,?,?)',(name1,email,gender,country,prog,))
   conn.commit()
   reset()
   
             
label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root,textvar=Fullname)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Email",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root,textvar=Email)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
label_3.place(x=70,y=230)

rb_1 = Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
rb_2 = Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)

label_4 = Label(root, text="country",width=20,font=("bold", 10))
label_4.place(x=70,y=280)

list1 = ['Canada','India','UK','Nepal','Iceland','South Africa'];

list1 = ['Canada','India','UK','Nepal','Iceland','South Africa'];
c.set("Select the contry")
combo = ttk.Combobox(root, values= list1, textvar=c, width=15)
combo.place(x=240,y=280)

label_4 = Label(root, text="Programming",width=20,font=("bold", 10))
label_4.place(x=85,y=330)
var2= IntVar()
ch_1 = Checkbutton(root, text="java", variable=var1).place(x=235,y=330)

ch_2 = Checkbutton(root, text="python", variable=var2).place(x=290,y=330)

Button(root, text='Submit', width=20, bg='#1FC4F5', fg='white',command=database).place(x=180,y=380)

root.mainloop()
























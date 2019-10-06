import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import datetime
from subprocess import call

# root = tk.Tk()
# root.withdraw()
# messagebox.showinfo("Title", "a Tk MessageBox")

mydb=mysql.connector.connect(host="localhost",user="root",passwd="",
                             database="sagar")
mycursor=mydb.cursor()                             

win=tk.Tk()
win.title('Railway REservation')

heading=ttk.Label(win,text="Welcome to Indian Railways!!")
heading.grid(row=0,column=1)

source_label=ttk.Label(win,text="Enter the source station : ")
source_label.grid(row=1,column=0,sticky=tk.W)

src=tk.StringVar()
source_box=ttk.Entry(win,width=16,textvariable=src)
source_box.grid(row=1,column=1)
source_box.focus()

dest_label=ttk.Label(win,text="Enter the destination station : ")
dest_label.grid(row=2,column=0,sticky=tk.W)

dest=tk.StringVar()
dest_box=ttk.Entry(win,width=16,textvariable=dest)
dest_box.grid(row=2,column=1)
dest_box.focus()



def action():
    source=src.get()
    destination=dest.get()
    
    sql="SELECT * FROM train where Source=%s and Destination=%s"
    val=(source,destination)
    mycursor.execute(sql,val)
    temp =mycursor.fetchall()
    win.withdraw()
    messagebox.showinfo("Result", temp)
    win.deiconify()
    

submit_button=ttk.Button(win,text="Check",command=action)
submit_button.grid(row=3,column=0)

status_label=ttk.Label(win,text="Check the seat availablity : ")
status_label.grid(row=4,column=0,sticky=tk.W)

stat=tk.StringVar()
status_box=ttk.Entry(win,width=16,textvariable=stat)
status_box.grid(row=4,column=1)
status_box.focus()

def action2():
    status=stat.get()
    
    # sql="SELECT * FROM train_status where Number=%s"
    # val=(status)
   
    mycursor.execute("SELECT * FROM train_status where Number="+status)
    temp3 =mycursor.fetchall()
    print(temp3[0][1])
    win.withdraw()
    messagebox.showinfo("Result", "Sleeper Class : "+str(temp3[0][1])+"\n3rd AC : "+str(temp3[0][4]))
    win.deiconify()



submit_button=ttk.Button(win,text="Check",command=action2)
submit_button.grid(row=5,column=0)

ticket_label=ttk.Label(win,text="Want to book ticket.......")
ticket_label.grid(row=6,column=0,sticky=tk.W)

def action3():
    win.withdraw()
    call(["python", "usergui.py"])
    win.deiconify()

submit_button=ttk.Button(win,text="Click here",command=action3)
submit_button.grid(row=7,column=0)

cancel_label=ttk.Label(win,text="Want to cancel a ticket.......")
cancel_label.grid(row=8,column=0,sticky=tk.W)

def action4():
    win.withdraw()
    call(["python", "cancelgui.py"])
    win.deiconify()

submit_button=ttk.Button(win,text="Click here",command=action4)
submit_button.grid(row=9,column=0)

status_label=ttk.Label(win,text="Check your ticket status here.......")
status_label.grid(row=10,column=0,sticky=tk.W)

train_label=ttk.Label(win,text="Enter your booking Id: ")
train_label.grid(row=11,column=0,sticky=tk.W)

train=tk.StringVar()
train_box=ttk.Entry(win,width=16,textvariable=train)
train_box.grid(row=11,column=1)
train_box.focus()

def action5():
    train1=train.get()
    mycursor.execute("SELECT * FROM passenger where user_id="+train1)
    temp4 =mycursor.fetchall()
    print(temp4)
    win.withdraw()
    messagebox.showinfo("Result",temp4)
    win.deiconify()

submit_button=ttk.Button(win,text="Click here",command=action5)
submit_button.grid(row=12,column=0)

win.mainloop()
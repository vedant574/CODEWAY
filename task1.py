import tkinter as tk
from tkinter import *

# main window
screen = Tk()
screen.geometry("620x700")
screen.resizable(False, False)
screen['bg'] = '#E0C875'
screen.title("To Do List")

# function to add task
def add():
    job_text = JOB.get()
    if job_text:
        VIEW.insert(END, job_text)
        DUTY.delete(0,END)

#function to remove task
def remove():
    VIEW.delete(tk.ANCHOR)    

# ICON
ICON = PhotoImage(file="ghost.png")
screen.iconphoto(False, ICON)

# Heading
HEAD = Label(screen, text="Task", fg='#C56A36', bg='#EFA53D', font=('display', 30, "bold"), width=25)
HEAD.place(relx=0.012)

# input box
JOB = StringVar()
DUTY = Entry(screen, width=32, borderwidth=5, font=('system', 18), bd=2, textvariable=JOB)
DUTY.place(x=2, y=60)
DUTY.focus()

# display box
VIEW = Listbox(screen, font=('system', 18), width=32, height=17, borderwidth=2,
               cursor='pencil',selectforeground='#0B60BA' ,selectbackground='#96EFFF', bg='#FFFDB0')
VIEW.place(x=2, y=100)

#scrollbar to view up and down
VIEWBAR=Scrollbar(screen)
VIEWBAR.place(x=520,y=300)
VIEW.config(yscrollcommand=VIEWBAR.set)
VIEWBAR.config(command=VIEW.yview)

# button to add JOB
ADD = Button(screen, text="Add Task", pady=5, width=11, relief='raised', command=add).place(x=528, y=60)

#button to delete task
BIN = PhotoImage(file="bin.png")
DONE=Button(screen,image=BIN,borderwidth=0,width=80,bg= '#E0C875',relief='raised',command=remove).place(x=530,y=100)

screen.mainloop()

from tkinter import *
import random, string
import pyperclip

#initialize window
screen =Tk()
screen.geometry("500x300")
screen.resizable(FALSE,FALSE)
screen.title("PASSWORD GENERATOR")
screen.config(bg='#96E9C6')


#heading
heading = Label(screen,bg='#96E9C6',
                text = 'PASSWORD GENERATOR', 
                font ='arial 20 bold').place(x=10, y=8)
option = Label(screen,bg='#96E9C6',
               text = 'COMPLEXITY',
               font ='arial 15').place(x=300, y=40)

#user entry 
pass_label = Label(screen,bg='#96E9C6',
                   text = 'PASSWORD LENGTH',
                   font = 'arial 15').place(x=10, y=40)
pass_len = IntVar()
length = Spinbox(screen,from_ = 8, to_ = 32 , textvariable = pass_len , width = 15).place(x=12,y=70)

#options to select complexity
choice=IntVar(value='null')
weak=Radiobutton(screen,text='weak',value=1,variable=choice,font='calibri 15').place(x=300,y=75)
strong=Radiobutton(screen,text='strong',value=2,variable=choice,font='calibri 15').place(x=300,y=120)

#function to copy
def Copy_password():
    pyperclip.copy(pass_str.get())

# Generate function
pass_str = StringVar()

def Generator():
    global pass_len
    password = ''
    small=string.ascii_lowercase
    capital=string.ascii_uppercase
    numb=string.digits
    spec=string.punctuation
    if choice.get() == 2:  # Use choice.get() to get the value of IntVar
        combined = small + capital + numb + spec
        password = random.sample(combined, pass_len.get())
        pass_str.set(''.join(password))
    elif choice.get() == 1:  # Use choice.get() to get the value of IntVar
        combined = small + capital
        password = random.sample(combined, pass_len.get())
        pass_str.set(''.join(password))

#Generate button
Button(screen, text = "GENERATE PASSWORD" , command = Generator ).place(x=110,y=250)

Label(screen ,relief='sunken', textvariable = pass_str,width=45,font=('roman',14),fg='black').place(x=45,y=200)

Button(screen, text = 'COPY TO CLIPBOARD', command = Copy_password).place(x=249,y=250)



screen.mainloop()
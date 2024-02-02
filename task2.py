from tkinter import *

#function to select operation or number
def button_press(num):

    global equation_text

    equation_text = equation_text + str(num)

    equation_label.set(equation_text)

#functions to calculate
def equals():

    global equation_text

    try:

        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text = total

    except SyntaxError:

        equation_label.set("syntax error")

        equation_text = ""

    except ZeroDivisionError:

        equation_label.set("arithmetic error")

        equation_text = ""

#function to clear display
def clear():

    global equation_text

    equation_label.set("")

    equation_text = ""
#main window
Screen = Tk()
Screen.config(bg='#17161B')
Screen.title("Calculator program")
Screen.geometry("434x495")

equation_text = ""
equation_label = StringVar()

#display widget
display = Label(Screen, textvariable=equation_label, font=('consolas',19),
              bg="white", width=30, borderwidth=4, relief='sunken',height=2)
display.grid(columnspan=4,column=0,row=0)

#inset buttons
button1 = Button(Screen, text=1, height=3, width=8, font=('comic sans',14,'bold'),
                 command=lambda: button_press(1))
button1.grid(row=1, column=0)
button1.config(bg='#17161B',fg='#FFFFFF',bd=3)

button2 = Button(Screen, text=2, height=3, width=8, font=('comic sans',14,'bold'),
                 command=lambda: button_press(2))
button2.grid(row=1, column=1)
button2.config(bg='#17161B',fg='#FFFFFF',bd=3)

button3 = Button(Screen, text=3, height=3, width=8, font=('comic sans',14,'bold'),
                 command=lambda: button_press(3))
button3.grid(row=1, column=2)
button3.config(bg='#17161B',fg='#FFFFFF',bd=3)

button4 = Button(Screen, text=4, height=3, width=8, font=('comic sans',14,'bold'),
                 command=lambda: button_press(4))
button4.grid(row=2, column=0)
button4.config(bg='#17161B',fg='#FFFFFF',bd=3)

button5 = Button(Screen, text=5, height=3, width=8, font=('comic sans',14,'bold'),
                 command=lambda: button_press(5))
button5.grid(row=2, column=1)
button5.config(bg='#17161B',fg='#FFFFFF',bd=3)

button6 = Button(Screen, text=6, height=3, width=8, font=('comic sans',14,'bold'),
                 command=lambda: button_press(6))
button6.grid(row=2, column=2)
button6.config(bg='#17161B',fg='#FFFFFF',bd=3)

button7 = Button(Screen, text=7, height=3, width=8, font=('comic sans',14,'bold'),
                 command=lambda: button_press(7))
button7.grid(row=3, column=0)
button7.config(bg='#17161B',fg='#FFFFFF',bd=3)

button8 = Button(Screen, text=8, height=3, width=8, font=('comic sans',14,'bold'),
                 command=lambda: button_press(8))
button8.grid(row=3, column=1)
button8.config(bg='#17161B',fg='#FFFFFF',bd=3)

button9 = Button(Screen, text=9, height=3, width=8, font=('comic sans',14,'bold'),
                 command=lambda: button_press(9))
button9.grid(row=3, column=2)
button9.config(bg='#17161B',fg='#FFFFFF',bd=3)

button0 = Button(Screen, text=0, height=3, width=8, font=('comic sans',14,'bold'),
                 command=lambda: button_press(0))
button0.grid(row=4, column=0)
button0.config(bg='#17161B',fg='#FFFFFF',bd=3)

plus = Button(Screen, text='+', height=3, width=8, font=('comic sans',14,'bold'),
                 command=lambda: button_press('+'))
plus.grid(row=1, column=3)
plus.config(bg='#17161B',fg='#FFFFFF',bd=3)

minus = Button(Screen, text='-', height=3, width=8, font=('comic sans',14,'bold'),
                 command=lambda: button_press('-'))
minus.grid(row=2, column=3)
minus.config(bg='#17161B',fg='#FFFFFF',bd=3)

multiply = Button(Screen, text='*', height=3, width=8, font=('comic sans',14,'bold'),
                 command=lambda: button_press('*'))
multiply.grid(row=3, column=3)
multiply.config(bg='#17161B',fg='#FFFFFF',bd=3)

divide = Button(Screen, text='/', height=3, width=8, font=('comic sans',14,'bold'),
                 command=lambda: button_press('/'))
divide.grid(row=4, column=3)
divide.config(bg='#17161B',fg='#FFFFFF',bd=3)

equal = Button(Screen, text='=', height=3, width=17, font=('comic sans',14,'bold'),
                 command=equals)
equal.grid(row=5, column=2,columnspan=2)
equal.config(bg='#FC6736',fg='#FFFFFF',bd=3)

left_bracket = Button(Screen, text='(', height=3, width=8, font=('comic sans',14,'bold'),
                 command=lambda: button_press('('))
left_bracket.grid(row=4, column=1)
left_bracket.config(bg='#17161B',fg='#FFFFFF',bd=3)

right_bracket = Button(Screen, text=')', height=3, width=8, font=('comic sans',14,'bold'),
                 command=lambda: button_press(')'))
right_bracket.grid(row=4, column=2)
right_bracket.config(bg='#17161B',fg='#FFFFFF',bd=3)

remove = Button(Screen, text='Clear', height=3, width=17, font=('comic sans',14,'bold'),
                 command=clear)
remove.grid(columnspan=2,row=5,column=0)
remove.config(bg='#79018C',fg='#FFFFFF',bd=3)

Screen.mainloop()
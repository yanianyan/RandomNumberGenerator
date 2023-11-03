from tkinter import *
import random

win = Tk()
win.title("Random Number Generator 1-100")
win.geometry("550x450")
win.grid()

def randomnum(event):
    value=random.randint(1,101)
    print(value)
    updateDisplay(value)

def updateDisplay(myString):
    displayVariable.set(myString)
#GUI

title_label = Label(win, text="Random Number Generator", font=("Comic Sans MS", 20, "bold"))
title_label.pack()
button_1 =Button(win, text="Click Here")
button_1.bind("<1>",randomnum)
button_1.pack()
displayVariable = StringVar()
Label1 = Label(win, textvariable = displayVariable, font=("Comic Sans MS", 20, "bold"))
Label1.pack(side=TOP, padx=30, pady=30)

win.mainloop()

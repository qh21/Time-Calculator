################################################
from tkinter import *
import tkinter.font
import numpy as np

root = Tk()
label= tkinter.Label()
root.title('Time Calculator')

root.geometry('750x650')
root.config(bg='#131417')




Desired_font = tkinter.font.Font( family = "Roboto Mono", 
                                 size = 10, 
                                 weight = "bold")

################################################
secondsCounter = 0
minutesCounter = 0 
houresCounter = 0

secondsCounter2 = 0

def clearResults():
    global label1
    label1.destroy()

def displayResult1():

    global label1
    label1 = Label(root, text='Houres: 0 , Minutes: 0 , Seconds: 0\t',bg='#131417',fg='#fff',font=Desired_font)
    label1.place(x=15,y=80)


def displayResult2(secondsCounter,minutesCounter,houresCounter):
    global label1
    #print(f"{houresCounter}:{minutesCounter}:{secondsCounter}")
    label1 = Label(root, text=f'Houres: {houresCounter} , Minutes: {minutesCounter} , Seconds: {secondsCounter}\t',bg='#131417',fg='#fff',font=Desired_font)
    label1.place(x=15,y=80)


def clearEntry():
    secondsInput.delete(0, END)
    minutersInput.delete(0, END)
    houresInput.delete(0, END)

def TimeCalcFunction(seconds,minutes,houres):
    reset()
    global secondsCounter,minutesCounter,houresCounter
    secondsCounter+=seconds
    if  seconds>0:
        while secondsCounter>=60:
            secondsCounter-=60
            minutesCounter+=1
        while minutesCounter>=60:
            minutesCounter-=60
            houresCounter+=1
    elif  seconds<0:
        while secondsCounter<=-60:
            secondsCounter+=60
            minutesCounter-=1        
        while minutesCounter<=-60:
            minutesCounter+=60
            houresCounter-=1
    while houresCounter<0:
        houresCounter+=1
        minutesCounter-=60
    while minutesCounter<0:
        minutesCounter+=1
        secondsCounter-=60
    while secondsCounter<=-60:
        secondsCounter+=60
        minutesCounter-=1        
    while minutesCounter<=-60:
        minutesCounter+=60
        houresCounter-=1
    clearResults()
    displayResult2(secondsCounter,minutesCounter,houresCounter)
    clearEntry()


def clickEnter(event):
    clearResults()
    temp1(secondsInput.get(),minutersInput.get(),houresInput.get())
    clearEntry()



def reset():
    global secondsCounter
    global minutesCounter
    global houresCounter
    secondsCounter = 0
    minutesCounter = 0
    houresCounter = 0
    clearEntry()

def reset2():
    clearResults()
    global secondsCounter2
    global secondsCounter
    global minutesCounter
    global houresCounter
    secondsCounter2 = 0
    secondsCounter = 0
    minutesCounter = 0
    houresCounter = 0
    clearEntry()
    displayResult1()

houresInput = Entry(root,width=10)
houresInput.place(x=20,y=10)
minutersInput = Entry(root,width=10)
minutersInput.place(x=100,y=10)
secondsInput = Entry(root,width=10)
secondsInput.place(x=180,y=10)

options_list2 = {0:"+",1:"-"}
value_inside2 = tkinter.StringVar(root)
value_inside2.set(options_list2[0])
question_menu2 = OptionMenu(root,value_inside2, *options_list2.values())
question_menu2.place(x=260,y=10)

resetButton = Button(root, text='Reset',command=lambda:[reset2()])
resetButton.place(x=340,y=10)

calculateButton = Button(root, text='Calculate',command=lambda:[clearResults(),temp1(secondsInput.get(),minutersInput.get(),houresInput.get())])#''',sendToFile()'''

root.bind('<Return>',clickEnter)

def temp1(seconds,minutes,houres):
    global secondsCounter
    global secondsCounter2
    if seconds == "":
        seconds = 0
    if minutes == "":
        minutes = 0
    if houres == "":
        houres = 0
    seconds=int(seconds);minutes=int(minutes);houres=int(houres)
    while houres>=1:
        houres-=1
        seconds+=3600
    while minutes>=1:
        minutes-=1
        seconds+=60
    if  format(value_inside2.get())==options_list2[0]:
        secondsCounter2 += seconds

    elif  format(value_inside2.get())==options_list2[1]:       
        secondsCounter2 -= seconds
    print("Counter:\t",secondsCounter2)
    TimeCalcFunction(secondsCounter2,0,0)

calculateButton.place(x=400,y=10)

label1 = Label(root, text=f'Houres: {houresCounter} , Minutes: {minutesCounter} , Seconds: {secondsCounter}\t',bg='#131417',fg='#fff',font=Desired_font)
label1.place(x=15,y=80)


root.mainloop()
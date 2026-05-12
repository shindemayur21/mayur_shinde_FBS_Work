from tkinter import *
from tkinter import messagebox


def changeBg():
    val = x.get()
    if (val == 1):
        window.config(bg='black')
    elif (val == 2):
        window.config(bg='green')
    elif (val == 3):
        window.config(bg='yellow')
    else:
        messagebox.showwarning(message='No color selected')


window = Tk()
window.geometry('300x400')

x = IntVar()

txt = Label(window, text='Please select color : ')
txt.pack()

rd1 = Radiobutton(window, text='black', variable=x, value=1)
rd1.pack()

rd2 = Radiobutton(window, text='green', variable=x, value=2)
rd2.pack()

rd3 = Radiobutton(window, text='yellow', variable=x, value=3)
rd3.pack()

btn = Button(window, text='Apply', command=changeBg)
btn.pack()

window.mainloop()

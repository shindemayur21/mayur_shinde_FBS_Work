from tkinter import *
from tkinter import messagebox


def submit():
    val1 = x.get()
    val2 = y.get()
    val3 = z.get()

    course = ''
    if (val1 == 1):
        course += 'Python\n'
    if (val2 == 1):
        course += 'Java\n'
    if (val3 == 1):
        course += 'Testing\n'
    if (course):
        messagebox.showinfo(message=course)
    else:
        messagebox.showwarning(message='No course selected')


window = Tk()
window.geometry('300x400')

x = IntVar()
y = IntVar()
z = IntVar()

txt = Label(window, text='Please select course : ')
txt.pack()

chk1 = Checkbutton(window, text='python', variable=x)
chk1.pack()

chk2 = Checkbutton(window, text='java', variable=y)
chk2.pack()

chk3 = Checkbutton(window, text='Testing', variable=z)
chk3.pack()

btn = Button(window, text='Submit', command=submit)
btn.pack()

window.mainloop()

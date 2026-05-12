from tkinter import *

window = Tk()

window.geometry('300x400')
window.title('First program')
window.config(bg='#1e1e2f')

txt = Label(
    window,
    text='Hello World',
    font=('Arial', 18, 'bold'),
    bg='#1e1e2f',
    fg='cyan',
    pady=20)

txt.pack()

window.mainloop()

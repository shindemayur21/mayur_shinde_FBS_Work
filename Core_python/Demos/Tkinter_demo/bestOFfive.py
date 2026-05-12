from tkinter import *
from tkinter import messagebox


def percent():
    num1 = int(e1.get())
    num2 = int(e2.get())
    num3 = int(e3.get())
    num4 = int(e4.get())
    num5 = int(e5.get())
    num6 = int(e6.get())

    top5 = sorted([num1, num2, num3, num4, num5, num6], reverse=True)[:5]

    perc = (sum(top5) / 500) * 100

    messagebox.showinfo(message=f"Percentage = {perc:.2f}%")


window = Tk()

window.title("Top 5 sub marks")
window.geometry("300x350")


Label(window, text="Enter First Number").pack()
e1 = Entry(window)
e1.pack()

Label(window, text="Enter Second Number").pack()
e2 = Entry(window)
e2.pack()

Label(window, text="Enter Third Number").pack()
e3 = Entry(window)
e3.pack()

Label(window, text="Enter Fourth Number").pack()
e4 = Entry(window)
e4.pack()

Label(window, text="Enter Fifth Number").pack()
e5 = Entry(window)
e5.pack()

Label(window, text="Enter Sixth Number").pack()
e6 = Entry(window)
e6.pack()


Button(window, text="Percent", command=percent).pack(pady=10)

window.mainloop()

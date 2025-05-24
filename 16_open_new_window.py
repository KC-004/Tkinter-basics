from tkinter import *


def create_window():
    new_window = Tk()    # OR use Topleve()

    old_window.destroy()

old_window = Tk()
old_window.title("Opening new Window")

Button(text="Create new window", font=('clover', 25), command=create_window).pack()

old_window.mainloop()
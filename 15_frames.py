from tkinter import *


window = Tk()
window.title("Frames")

frame = Frame(window, bg='gray',padx=10, pady=10, bd=5, relief=SUNKEN)


btn_W = Button(frame, text="W", font=("conslas", 25), width=3)
btn_A = Button(frame, text="A", font=("conslas", 25), width=3)
btn_S = Button(frame, text="S", font=("conslas", 25), width=3)
btn_D = Button(frame, text="D", font=("conslas", 25), width=3)

btn_W.pack(side=TOP)
btn_A.pack(side=LEFT)
btn_S.pack(side=LEFT)
btn_D.pack(side=LEFT)

frame.place(x=250, y=250)

window.mainloop()
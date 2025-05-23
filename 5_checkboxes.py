
from tkinter import *
from PIL import Image, ImageTk
def display():

    if ( x.get() == 1 and y.get() == 1):
        print("I both python and java.")
    elif (x.get() == 1 and y.get() == 0):
        print("I like python.")
    elif (x.get() == 0 and y.get() == 1):
        print("I like Java")
    else:
        print("I don't like either.")

window = Tk()
window.title('Checkboxes')

x = IntVar()
y = IntVar()

#check box 1
image = Image.open("imgs/python.jpeg")
image = image.resize((50, 50))
image = ImageTk.PhotoImage(image)

checkbox = Checkbutton(window, text='Python', variable=x, onvalue=1, offvalue=0, command=display)
checkbox.config(font=('futura', 30, 'bold'),
                image=image,
                compound=LEFT,
                padx=10,
                pady=10,
                background='black',
                activebackground='black',
                foreground='blue',
                activeforeground='blue',
                anchor='w',
                width=300
                )

# Check box 2
image2 = Image.open("imgs/java.png")
image2 = image2.resize((50, 50))
image2 = ImageTk.PhotoImage(image2)

chekcbox2 = Checkbutton(window, text='Java', variable=y, onvalue=1, offvalue=0, command=display)
chekcbox2.config(font=('futura', 30, 'bold'),
                image=image2,
                compound=LEFT,
                padx=10,
                pady=10,
                background='black',
                activebackground='black',
                foreground='blue',
                activeforeground='blue',
                anchor='w',
                width=300,
                )

checkbox.pack(anchor='w')
chekcbox2.pack(anchor='w')

window.mainloop()
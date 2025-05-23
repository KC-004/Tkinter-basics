from tkinter import *
from PIL import Image, ImageTk


#functions

def open():
    print("File opened!")
def save():
    print("File saved!")
def edit():
    print('Editing file')


window = Tk()
window.title('Menubars')

menubar = Menu(window)
window.config(menu=menubar)

img = Image.open('icon.png')
img = img.resize((20, 20))
img = ImageTk.PhotoImage(img)


filemenu = Menu(menubar, tearoff=0, font=('times new roman', 20, 'italic'))
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Open', command=open, image=img, compound='left')
filemenu.add_command(label='Save', command=save)
filemenu.add_command(label='Quit', command=quit)


editmenu = Menu(menubar, tearoff=0, font=('times new roman', 20, 'italic'))
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Edit file', command=edit)
editmenu.add_command(label='Save file', command=save)
editmenu.add_command(label='Exit', command=quit)


window.mainloop()

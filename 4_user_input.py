
from tkinter import *

# methods
def submit():

    user_name = entry.get()
    print('Hello',user_name)

def delete():

    entry.delete(0, END)

def backspace():

    entry.delete(len(entry.get())-1, END)


window = Tk()
window.title('User Input')
submit = Button(window, text='Submit', command=submit)

delete = Button(window, text='Delete', command=delete)

backspace = Button(window, text='backspace', command=backspace)
entry = Entry(window,
              font=('futura', 25, 'italic'),
              bg='black',
              fg='cyan',
              )
submit.pack(side=RIGHT)
delete.pack(side=RIGHT)
backspace.pack(side=RIGHT)
entry.pack()


window.mainloop()
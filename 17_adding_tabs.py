from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Adding new Tabs")

notebook = ttk.Notebook(window)  # manages a collection of windows/displays

tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1, text='Tab 1')
notebook.add(tab2, text='Tab 2')
notebook.pack(expand =True, fill="both")  # expand to fill the space not used || #fill will fill space in x and y axis

Label(tab1, text="Hello this is Tab no. 1", width=50, height=25).pack()
Label(tab2, text="Hello this is Tab no. 2", width=50, height=25).pack()

window.mainloop()
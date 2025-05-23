from tkinter import *
from tkinter import filedialog

''' Funtions'''
def open_file():
    file_path = filedialog.askopenfilename(initialdir="E:\\PRO_FILE\\Python\\Tkinter_Learning",
                                           title="Select a file",
                                           filetypes=(("text files", "*.txt"),
                                                      ("all files", "*.*"))
                                           )
    file = open(file_path, 'r')
    text = file.read()
    print(text)
    file.close()
''' GUI '''
window = Tk()
window.title("File Dialog")

''' Widgets '''
btn = Button(window,
             text='Open File',
             command=open_file
             )

''' Packing '''
btn.pack()

window.mainloop()
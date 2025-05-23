from tkinter import *
from tkinter import colorchooser

''' Functions '''
def change_color():
    color = colorchooser.askcolor()
    print(color)
    hex_color = color[1]
    print(hex_color)
    window.config(bg=hex_color)

    #window.config(bg=colorchooser.askcolor()[1])            # Above code in one line code

''' GUI '''
window = Tk()
window.title('Color Chooser')
window.geometry('500x500')

''' Widgets '''
btn = Button(window,
             text='BG Color',
             command=change_color
             )

''' Packing '''
btn.pack()

window.mainloop()

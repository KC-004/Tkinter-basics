from tkinter import *

''' Functions '''
def get_text():
    content = text.get(0.0, END)
    print(content)

''' GUI '''
window = Tk()
window.title('Text area')

''' Widgets '''
text = Text(window,
            font=('ink free', 20, 'bold'),
            bg='#d1fcd5',
            height=10,
            width=30,
            pady=10,
            padx=10,
            fg='brown'
            )
btn = Button(window,text='Submit',
             command=get_text
             )

''' Packing '''
text.pack()
btn.pack()

window.mainloop()
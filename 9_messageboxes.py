from tkinter import *
from tkinter import messagebox


def on_click():

    messagebox.showinfo(title='Information', message='This is a information box.')

    # messagebox.showerror(title='Error', message='This file has Error!.')

    # messagebox.showwarning(title='Warning', message='This file may contain virus.')

    # if messagebox.askokcancel(title='Ask ok cancel', message='Do you want pizza?'):
    #     print('Here is your pizza')
    # else:
    #     print('Why not?')

    # if messagebox.askyesno(title='Ask yes no', message='Do like coding?'):
    #     print('Nice :)')
    # else:
    #     print('Then why are you here  >:p')

    # answer = messagebox.askquestion(title='Ask question?', message='Do you like pineapple on pizza?')
    # if answer == 'yes':
    #     print('You have a bad taste in food.')
    # else:
    #     print('Neither do I :)')

    # answer = messagebox.askyesnocancel(title='Ask yes no cancel', message='Do you like cars?')
    # if answer == True:
    #     print('I like it too.')
    # elif answer == False:
    #     print('How can you not like it.')
    # else:
    #     print("Why don't you answer the question?")

    # if messagebox.askretrycancel(title='Retry cancel', message='Do you want to retry or cancel?'):
    #     print('Retrying....')
    # else:
    #     print('Cancelling....')

window = Tk()
window.title('Messageboxes')

click = Button(window,
               text='Click me!',
               command=on_click
               )
click.pack()

window.mainloop()

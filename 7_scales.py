from tkinter import *
from PIL import  Image, ImageTk
def get_temp():
    print(f'The temperature is {scale.get()}.')

def rezise_img(file_name):

    img = Image.open(file_name)
    img = img.resize((100, 100))
    img = ImageTk.PhotoImage(img)
    return img

window = Tk()
window.title('Scales')

window.config(background='black',
              pady=10,
              padx=50)

# images
fire = Label(window,
             text='🔥',
             font=('futura', 30),
             foreground='red',
             bg='black',
             pady=10
             )

# Widgets
snow = Label(window,
             text='❄',
             font=('futura', 30),
             foreground='cyan',
             bg='black',
             pady=10
             )

scale = Scale(window,
              from_=100,
              to=0,
              font=('cursive', 16),
              length=500,
              orient=VERTICAL,
              tickinterval=10,
              resolution=5,
              # showvalue=False,
              troughcolor='yellow',
              foreground='white',
              background='black'
              )

scale.set(((scale['from']-scale['to'])/2)+scale['to'])

button = Button(window,
                text='Submit',
                command=get_temp,
                font=('futura', 15, 'bold'),
                cursor='circle'
                )

# packing

fire.pack()
scale.pack()
snow.pack()
button.pack()

window.mainloop()
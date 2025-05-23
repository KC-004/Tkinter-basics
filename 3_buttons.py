
from tkinter import *
from PIL import Image, ImageTk

count = 0

def click():
    global count
    count += 1
    label.config(text=count)

window = Tk()
window.title("Buttons")

# Label
label = Label(window,
              text=count,
              font=('futura', 50, 'bold'))

# Button
button = Button(window,
                text="CLICK ME!",
                font=('futura', 30, 'bold'),
                bg='red',
                padx=10,
                pady=10,
                activebackground='#00ff00',
                )
image = Image.open("Icon.png")
image = image.resize((200,200))
image = ImageTk.PhotoImage(image)
button.config(image=image,
              compound='bottom',
              )
# button.config(state= DISABLED)   #This will disable the button
button.config(command=click)

# packing
label.pack()
button.pack()

window.mainloop()
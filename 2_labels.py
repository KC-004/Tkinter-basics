from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title("Labels")

image = Image.open("Icon.png")
image = image.resize((500, 500))

image = ImageTk.PhotoImage(image)

label = Label(window,
              text="Hello World",
              fg="orange",
              bg="black",
              font=('Ariel', 40, 'bold', 'italic',),
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=image,
              compound='bottom'
              )

label.pack()
window.mainloop()
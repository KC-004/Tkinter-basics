
from tkinter import *
from PIL import Image, ImageTk


food_list = ['Pizza', 'Burger', 'Medium Fries']

def order():
    if x.get() == 0:
        print("You ordered a pizza.")
    elif x.get() == 1:
        print("You ordered a Burger.")
    elif x.get() == 2:
        print("You ordered a Medium Fries.")
    else:
        print("Error!")



window = Tk()
window.title('Radiobuttons')

# image

def rezise_img(file_name):

    img = Image.open(file_name)
    img = img.resize((100, 100))
    img = ImageTk.PhotoImage(img)
    return img

pizza = rezise_img('imgs/pizza.png')
burger = rezise_img('imgs/burger.png')
fries = rezise_img('imgs/fries.png')
food_images = [pizza, burger, fries]

x = IntVar()

for item in range(len(food_list)):
    radiobutton = Radiobutton(window,
                              text=food_list[item],
                              variable=x,
                              value=item,
                              font=('futura', 20, 'bold'),
                              padx=10,
                              pady=10,
                              image=food_images[item],
                              compound="left",
                              indicatoron=0,            #eliminates circle indicator
                              width=350,
                              background='black',
                              foreground='white',
                              activebackground='green',
                              activeforeground='white',
                              selectcolor='green',       # Changes the color of selected item
                              command=order,
                              anchor='w'
                              )
    radiobutton.pack(anchor=W)

window.mainloop()
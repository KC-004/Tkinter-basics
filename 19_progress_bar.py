import time
from tkinter import *
from tkinter.ttk import *


def start():
    GB = 132
    downloaded = 0
    speed = 1
    while downloaded < GB:
        time.sleep(0.05)
        bar['value'] += (speed/GB) * 100
        downloaded += speed
        percent.set(str(int((downloaded/GB)*100))+"%")
        text.set(f"{downloaded}/{GB} GB completed!")
        window.update_idletasks()


window = Tk()
window.title("Progress bar")

percent = StringVar()
text = StringVar()

bar = Progressbar(window, orient="horizontal", length=300)
bar.pack(pady=10)

Label(window, textvariable=percent).pack()
Label(window, textvariable=text).pack()

Button(window, text="Download", command=start).pack()

window.mainloop()

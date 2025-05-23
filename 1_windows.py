
from tkinter import *

window = Tk()
window.geometry("500x500")                  # setting windows size
window.title("Windows")                    # Setting windows title

# To Change the ICON
icon = PhotoImage(file="Icon.png")          # Tkinter only accepts PhotoImage so we need to convert img into this formaete
window.iconphoto(True, icon)         # Setting Icon


window.config(background="#4ad2ed")         # Setting Background color

window.mainloop()


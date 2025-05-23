from tkinter import *
from tkinter import filedialog


def write_file():
    file = filedialog.asksaveasfile(defaultextension='.txt',
                                    initialdir="E:\PRO_FILE\Python\Tkinter_Learning",
                                    title='saving file',
                                    filetypes=[
                                        ("text file", "*.txt"),
                                        ("All files", "*.*")

                                               ]
                                    )
    print(file)
    if file is None:
        return

    file.write(text.get(1.0, END))
    file.close()

window = Tk()
window.title('Save file (filedialog')

text = Text()
btn = Button(text='Submit', command=write_file)
text.pack()
btn.pack()

window.mainloop()

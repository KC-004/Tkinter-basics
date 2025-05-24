from tkinter import *



window = Tk()
window.title("Canvases")

canvas = Canvas(window, width=500, height=500, bg='black')
#
# canvas.create_line(0, 0, 500, 500, fill="red", width=10)
# canvas.create_line(0, 500, 500, 0, fill="cyan", width=5)
# canvas.create_rectangle(100, 100, 450,350, fill="violet", outline='yellow')
#
# points = [250, 0, 0, 500, 500, 500]
# canvas.create_polygon(points, fill='purple', outline='white', width=5)
#
# canvas.create_arc(0, 0, 500, 500, style=PIESLICE, fill="green", start=90, extent=180)

'''creating pokiball'''
canvas.create_arc(0, 0, 500, 500, fill="white", extent=180, start= 180, width=10)
canvas.create_arc(0, 0, 500, 500, fill="red", extent=180, width=10)
canvas.create_oval(190, 190, 310, 310, fill="white", width=10)
canvas.pack()

window.mainloop()
from tkinter import *
master = Tk()
w = Canvas(master, width=400, height=10)
w.pack()
canvas_height=10
canvas_width=800
y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y )
mainloop()
from tkinter import *

root=Tk()

num1=StringVar()
num2=StringVar()

value1=Scale(root,from_=0,to=100,variable=num1)
value1.pack()
value2=Scale(root,from_=0,to=100,orient=HORIZONTAL,variable=num2)
value2.pack()

root.mainloop()
from tkinter import *
from tkinter.ttk import *

root = Tk()

frame=Frame(root)
frame.pack()

#frame inside the root windows
#it will help to creat a button and other importent applicattion
#with in the frame 
#Frame content is stored in the frame variable
#it will help to edit the frame content
#frame.pack() function are use to display the frame with in the root windows

button=Button(root,text='Enter')
#Button function are used to make button in the frame
#this button content are stroed in the button variable it will help to edit the button content
#button.pack() function are used to display the button in the root windows 
#by default thr button is placed in the top middel


button.pack()




root.mainloop()
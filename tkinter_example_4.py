from tkinter import *
from tkinter.ttk import *

root=Tk()

#pack() function are used to put the row and column values 
#pack(row=value,column=value)
#some other widgets are  grid() and the place()
# the grid( )function are used to put the 2D value like hight value of the Button and also the depth value of the Button
#place() function are used to .........................


root.title("Tkinter windows 4")
root.geometry("100x100")
#the geometry are use to set the fixed size the given root windows

button=Button(root,text='Enter',command=root.destroy)

#command fuction are use to make a working button
#if you enter the button the root windows is closed 
#bg set the normal backgrounf color
#command is use to call the function
#font to set the font on the button label
#image  to set the image on the button
#width to set the width of the button
# height to set the height of the button
# activebackground is set the backgroundcolor when button is under the curser
# activeforeground is set the foreground color to the button os under the cursor 

button.pack(side='top')




root.mainloop()

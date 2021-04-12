from tkinter import *
from tkinter.ttk import *

root=Tk()

root.title("this is the 5th windows")
root.geometry("500x500")

label=Label(root,text='my name is umesha ramesha hugger')
label.grid()

def entered():
    label.configure(text='you jest cliked the button')
#the configure function are use to make the configure the label function
#  . opareter are used to accesse the label content
#grid function is the geometry manager
#inside the grid (row=value,column=value)
#its like a array type


button=Button(root,text='Enter',command=entered)
button.grid(row=1,column=1)


root.mainloop()
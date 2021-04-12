from tkinter import *
from tkinter.ttk import *

root=Tk()
root.title('this is the 6th windows')
root.geometry("600x600")

label=Label(root,text='Are you umesha')
label.grid()

def entered():
    label.configure(text='you entered!')

button=Button(root,text='Yes',command=entered)
button.grid(row=0,column=1)



root.mainloop()
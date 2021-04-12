from tkinter import *
from tkinter.ttk import *

root=Tk()

root.title("this the 16th windows")
root.geometry('900x900')
label=Label(root,text='you enter the umesha')


list_box=Listbox(root)
list_box.insert(1,'umesha')
list_box.insert(2,'ramesha')
list_box.insert(3,'hugger')
list_box.insert(4,'angaragatti')
list_box.insert(5,'hosakatti')

list_box.pack()


root.mainloop()
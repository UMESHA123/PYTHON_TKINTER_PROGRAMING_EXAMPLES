from tkinter import *

root=Tk()
label=Label(root,text='entred')
label.grid()
def entred():
    label.configure(width='20')

    
menu=Menu(root)
item1=Menu(menu)
menu.add_cascade(label='File',menu=item1)
item1.add_command(label='New',command=entred)
item1.add_command(label='edit')
item1.add_command(label='copy')
item1.add_separator()
item1.add_command(label='Exit', command=root.quit)
root.config(menu=menu)

def entred():
    label.configure(width='20')

root.mainloop()
from tkinter import *

root=Tk()
root.title('this the 12th windows ')
root.geometry('600x600')

variable1=IntVar()
variable2=IntVar()

click=Checkbutton(root,text='Male',variable=variable1)
click.grid(row=0,column=0)
click=Checkbutton(root,text='Female',variable=variable2)
click.grid(row=0,column=1)


root.mainloop()
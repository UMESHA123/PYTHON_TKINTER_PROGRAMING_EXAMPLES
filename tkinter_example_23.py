from tkinter import *

root=Tk()
root.title('This is the 23th windows')
root.geometry('900x900')

top=Toplevel()
top.title('This is the top level windows ')
top.geometry('300x300')
label=Label(top,text='I am umesha. i love programing')
label.grid()



root.mainloop()
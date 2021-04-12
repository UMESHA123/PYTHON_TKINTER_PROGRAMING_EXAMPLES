from tkinter import *
from tkinter.ttk import *
root=Tk()
root.title('This is the 26th windows')
root.geometry('900x900')

label=Label(root,text='I AM UMESHA RAMESHA HUGGER',font=('Verdana',15))
label.pack(side=TOP,pady=10)

photo=PhotoImage(file=r'C:\Users\acer\Desktop\python\python\menu.png')
button=Button(root,text='Enter me!',image=photo)
button.pack()

root.mainloop()
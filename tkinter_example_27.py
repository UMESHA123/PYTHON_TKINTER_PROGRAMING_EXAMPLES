from tkinter import *
from tkinter.ttk import*


root=Tk()
root.title('This is the 27th windows')
root.geometry('900x900')
label=Label(root,text='click the below the button to enter',font=('Algerian',10))
label.pack(side=TOP,pady=10)

photo=PhotoImage(file=r'C:\Users\acer\Desktop\python\python\icon\arrow.png')
photoimage=photo.subsample(30,30)
button=Button(root,text='click',image=photoimage,compound=LEFT)
button.pack(side=TOP)



root.mainloop()
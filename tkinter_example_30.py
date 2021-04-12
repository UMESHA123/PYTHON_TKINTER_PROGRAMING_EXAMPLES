from tkinter import *

root=Tk()
root.title('tHIS IS THE 30TH WINDOWS')
root.geometry('900x900')
value1=StringVar(root,'1')
value2=StringVar(root,'1')
value3=StringVar(root,'1')
value4=StringVar(root,'1')

radiobutton1=Radiobutton(root,text='Radiobutton 1',bg='light blue',fg='red',indicator=0,variable=value1)
radiobutton1.pack(fill=X,ipady=10)
radiobutton2=Radiobutton(root,text='Radiobutton 1',bg='light blue',fg='red',indicator=0,variable=value2)
radiobutton2.pack(fill=X ,ipady=10)
radiobutton3=Radiobutton(root,text='Radiobutton 1',bg='light blue',fg='red',indicator=0,variable=value3)
radiobutton3.pack(fill=X,ipady=10)
radiobutton4=Radiobutton(root,text='Radiobutton 1',bg='light blue',fg='red',indicator=0,variable=value4)
radiobutton4.pack(fill=X ,ipady=10)


root.mainloop()
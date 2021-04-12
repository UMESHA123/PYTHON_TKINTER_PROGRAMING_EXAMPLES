from tkinter import *

root=Tk()

root.title('this is the 8th windows')
root.geometry('600x600')

label=Label(root,text='are american')
label.grid()
def entered():
    label.configure(text='you entred')
    txt='you entred text is'+ input1.get()
#the get()function are used to accesse the entred text in the entry box

input1=Entry(root,width=20)
# the width defines the length of the entry box
#input1 is the variable is used to store the entry box content

input1.grid(row=0,column=1)

button=Button(root,text='Enter',bd='1',fg='red',bg='#33ccff',command=entered)
button.grid(row=0,column=2)
#fg is the font background color
#bd is the 2d hight i.e depth of the button
#bg the background color

root.mainloop()
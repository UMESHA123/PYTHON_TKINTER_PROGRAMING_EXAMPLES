from tkinter import *


root=Tk()
root.title('this is the 7th windows')
root.geometry('600x600')

label=Label(root,text='are you indian')
label.grid()

def entered():
    label.configure(text='you entered')

#colore gradient linke   https://en.wikipedia.org/wiki/Color_gradient
button=Button(root,text='Entered',fg='red',bg='#00ff00',bd='1',command=entered)
button.grid(row=0,column=1)

root.mainloop()

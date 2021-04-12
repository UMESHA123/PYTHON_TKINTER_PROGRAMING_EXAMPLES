from tkinter import *

root=Tk()
root.title('This is the 10th windows')

root.geometry('600x600')
menu=Menu(root)
item1=Menu(menu)
item1.add_command(label='New file')
item1.add_command(label='New window')
item1.add_command(label='Open file')
item1.add_command(label='Open folder')
item1.add_command(label='Open Workspace')
item1.add_command(label='save file')
item1.add_command(label='save file as')
menu.add_cascade(label='File',menu=item1)

item2=Menu(menu)
item2.add_command(label='Undo')
item2.add_command(label='Redo')
item2.add_command(label='Cut')
item2.add_command(label='Copy')
item2.add_command(label='Paste')
item2.add_command(label='Find')
item2.add_command(label='Replace')
menu.add_cascade(label='Edit',menu=item2)

item3=Menu(menu)
item3.add_command(label='Start debuging')
item3.add_command(label='Run without debuging')
item3.add_command(label='Stop debuging')
item3.add_command(label='Restart debuging')
item3.add_command(label='Open the configuration')
item3.add_command(label='Add the configuration')
item3.add_command(label='New Breack point')
menu.add_cascade(label='Run',menu=item3)
root.config(menu=menu)

label=Label(root,text='Are you intrested in the programing ')
label.grid(row=0,column=0)

text1=Entry(root,width=30)
text1.grid(row=0,column=1)

def entred():
    label.configure(text='you clicked the button')


button=Button(root,text='enter',fg='red',bd='1',bg='#33ccff',command=entred)
button.grid(row=0,column=2)

root.mainloop()
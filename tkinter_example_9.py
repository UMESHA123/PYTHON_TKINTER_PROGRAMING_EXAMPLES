from tkinter import *

root=Tk()
root.title('this is the 9th windows')
root.geometry('600x600')
#Menu fuction are used to creat a menu 
#menu is the variable it stors the Menu content

menu=Menu(root)
item=Menu(menu)
item.add_command(label='New file-1')
item.add_command(label='New file-2')
item.add_command(label='New file-3')
item.add_command(label='New file-4')
item.add_command(label='New file-5')
#add_commad is the new item with in the file
menu.add_cascade(label='File',menu=item)

#add_cascade are used to cascade the menu into the root windows
#label are used to display the text are image

root.config(menu=menu)


label=Label(root,text='are you human')
label.grid(row=0,column=0)
def entered():
    label.configure(text='you jest press the button')


entry=Entry(root,width=30)
entry.grid(row=0,column=1)

button=Button(root,text='Yes enter her!',command=entered)
button.grid(row=0,column=3)

root.mainloop()

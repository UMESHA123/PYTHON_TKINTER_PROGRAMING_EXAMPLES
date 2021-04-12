from tkinter import *
root=Tk()
root.title('This is the 21th windows')
root.geometry('900x900')

scrollbar=Scrollbar(root)
scrollbar.pack(side=LEFT,fill=Y)

mylist=Listbox(root,yscrollcommand=scrollbar.set)

for i in range(100):
    mylist.insert(END,'I AM FROM ANGARAGATTI'+str(i))
mylist.pack(side=LEFT,fill=BOTH)
scrollbar.config(command=mylist.yview)    


root.mainloop()
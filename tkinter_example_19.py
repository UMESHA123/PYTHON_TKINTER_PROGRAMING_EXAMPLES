from tkinter import *

root=Tk()
root.title('this is the 19th windows')
root.geometry('1800x720')
male=IntVar()
female=IntVar()
rediobutton_male=Radiobutton(root,text='male',fg='red',variable=male)
rediobutton_male.grid()
rediobutton_female=Radiobutton(root,text='female',fg='lightgreen',variable=female)
rediobutton_female.grid()



root.mainloop()
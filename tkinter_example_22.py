from tkinter import*
root=Tk()
root.title('This is the 22th windows')
root.geometry('900x900')

text1=Text(root,height=10,width=80,bd='1')
text1.pack()

text1.insert(END,'PRACTICAL HOAMONIC ANAYSIS\n')
text1.insert(END,'ENTER YOU NAME :\n')
text1.insert(END,'ENTER YOU LOST NAME :')


root.mainloop()
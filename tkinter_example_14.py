from tkinter import *

root =Tk()
root.title('this is the 14th windows')
root.geometry('600x600')

frame=Frame(root)
frame.pack()

redbutton=Button(frame,text='enter',fg='red')
redbutton.pack(side=LEFT)

greenbutton=Button(frame,text='green enter',fg='blue')
greenbutton.pack(side=LEFT)

bluebutton=Button(frame,text='Blue enter',fg='brown')
bluebutton.pack(side=LEFT)

blackbutton=Button(frame,text='Black button',fg='black')
blackbutton.pack(side=BOTTOM)


root.mainloop()

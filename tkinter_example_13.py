from tkinter import *

root=Tk()
root.title('this is the 13th windows')
root.geometry('600x600')

variable1=StringVar()
variable2=StringVar()

label=Label(root,text=variable1.get())
label.grid(row='6',column='1')
def entered():
    label.configure(text='you jest click the button')

label1=Label(root,text='Enter the first name').grid(row=0,column=0)
label2=Label(root,text='Enter the second name').grid(row=1,column=0)

entry1=Entry(root,width='30').grid(row=0,column=1)
entry2=Entry(root,width='30').grid(row=1,column=1)

button=Button(root,text='Enter her!',bd='1',command=entered)
button.grid(row=4,column=1)


root.mainloop()
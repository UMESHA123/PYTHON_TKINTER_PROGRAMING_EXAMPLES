from tkinter import *

root=Tk()

root.title('this is the 18th windows')
root.geometry('1800x720')

message=Message(root,text='this is the message')
message.config(bg='lightgreen')
message.pack()

message1=Message(root,text='this is the other message',bg='green')
message1.pack()


message2=Message(root,text='this is the one more message',fg='black',bg='lightgreen')
message2.pack()
root.mainloop()
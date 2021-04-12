from tkinter import *
from tkinter.ttk import *

root=Tk()
root.title('this the 28th windows')
root.geometry("900x900")
progressbar=Progressbar(root,orient=HORIZONTAL,length=400,mode='determinate')



def bar():
    import time
    progressbar['value']=10
    root.update_idletasks()
    time.sleep(1)

    progressbar['value']=20
    root.update_idletasks()
    time.sleep(1)
    
    progressbar['value']=30
    root.update_idletasks()
    time.sleep(1)

    progressbar['value']=40
    root.update_idletasks()
    time.sleep(1)

    progressbar['value']=50
    root.update_idletasks()
    time.sleep(1)

    progressbar['value']=60
    root.update_idletasks()
    time.sleep(1)

    progressbar['value']=70
    root.update_idletasks()
    time.sleep(1)

    progressbar['value']=80
    root.update_idletasks()
    time.sleep(1)

    progressbar['value']=90
    root.update_idletasks()
    time.sleep(1)

    progressbar['value']=100
    root.update_idletasks()
    time.sleep(1)

progressbar.pack(pady=10)
button=Button(root,text='START',command=bar)
button.pack(pady=30)

root.mainloop()
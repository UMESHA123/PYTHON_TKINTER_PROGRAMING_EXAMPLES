from tkinter import *
import math
import math,random,os
from tkinter import messagebox
class practical_harmonic_anysis:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1350x700+0+0')
        self.root.title("Practical Harmonic anysis")
        bg_color='#074463'
        title=Label(self.root,text="practical harmonic anaysis",bd=3,relief=GROOVE,bg=bg_color,fg='white',font=("times new roman",30,'bold'),pady=2).pack(fill=BOTH)
        
        
        self.x_value1=IntVar()
        self.x_value2=IntVar()
        self.x_value3=IntVar()
        self.x_value4=IntVar()
        self.x_value5=IntVar()
        self.x_value6=IntVar()
        self.x_value7=IntVar()
        self.x_value8=IntVar()
        self.x_value9=IntVar()
        self.x_value10=IntVar()
        self.x_value11=IntVar()
        self.x_value12=IntVar()
        self.x_value13=IntVar()
        self.x_value14=IntVar()
        
        self.y_value1=StringVar()
        self.y_value2=StringVar()
        self.y_value3=StringVar()
        self.y_value4=StringVar()
        self.y_value5=StringVar()
        self.y_value6=StringVar()
        self.y_value7=StringVar()
        self.y_value8=StringVar()
        self.y_value9=StringVar()
        self.y_value10=StringVar()
        self.y_value11=StringVar()
        self.y_value12=StringVar()
        self.y_value13=StringVar()
        self.y_value14=StringVar()
        
        self.x_value=IntVar()
        self.y_value=IntVar()
        self.hormonics=IntVar()
        
        self.y_value9=StringVar()
        self.total_value=StringVar()
        
        self.bill_data=StringVar()
        
        
        
        self.number_anaysis=StringVar()
        self.final_value1=StringVar()
        self.final_value=StringVar()
        
        
        self.cos_x_1=StringVar()
       
        
    
        
        F1=LabelFrame(self.root,bd=3,relief=GROOVE,text="USER INPUT 'X' AND 'Y' VALUE ",font=('Times new roman',15,'bold'),fg='gold',bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)
        
        x_value=Label(F1,text='X value',bg=bg_color,fg='white',font=("Times new roman",18,'bold')).grid(row=0,column=0,padx=20,pady=5)
        x_value_text=Entry(F1,width=20,textvariable=self.x_value,font='arial 15').grid(row=0,column=1,padx=10,pady=5)
     
        y_value=Label(F1,text='Y value',bg=bg_color,fg='white',font=("Times new roman",18,'bold')).grid(row=0,column=2,padx=20,pady=5)
        y_value_text=Entry(F1,width=20,textvariable=self.y_value,font='arial 15').grid(row=0,column=3,padx=10,pady=5)
        
        hormonics=Label(F1,text='number number of anysis',bg=bg_color,fg='white',font=("Times new roman",18,'bold')).grid(row=0,column=4,padx=20,pady=5)
        hormonics_text=Entry(F1,width=20,textvariable=self.hormonics,font='arial 15').grid(row=0,column=5,padx=10,pady=5)
        
        
    
        F2=LabelFrame(self.root,bd=3,relief=GROOVE,text="Enter X value",font=('Times new roman',15,'bold'),fg='gold',bg=bg_color)
        F2.place(x=1,y=150,width=200,height=400)

        x_value1=Label(F2,text='X1',font=('times new romen',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=0,column=0,padx=1,pady=1,sticky='w')
        x_value1=Entry(F2,width=10,textvariable=self.x_value1,font=('times new romen',16,'bold'),relief=SUNKEN).grid(row=0,column=1,padx=8,pady=2)

        x_value2=Label(F2,text='X2',font=('times new romen',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=1,column=0,padx=1,pady=1,sticky='w')
        x_value2=Entry(F2,width=10,textvariable=self.x_value2,font=('times new romen',16,'bold'),relief=SUNKEN).grid(row=1,column=1,padx=10,pady=2)
        
        x_value3=Label(F2,text='X3',font=('times new romen',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=2,column=0,padx=1,pady=1,sticky='w')
        x_value3=Entry(F2,width=10,textvariable=self.x_value3,font=('times new romen',16,'bold'),relief=SUNKEN).grid(row=2,column=1,padx=10,pady=2)
        
        x_value4=Label(F2,text='X4',font=('times new romen',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=3,column=0,padx=1,pady=1,sticky='w')
        x_value4=Entry(F2,width=10,textvariable=self.x_value4,font=('times new romen',16,'bold'),relief=SUNKEN).grid(row=3,column=1,padx=10,pady=2)
        
        x_value5=Label(F2,text='X5',font=('times new romen',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=4,column=0,padx=1,pady=1,sticky='w')
        x_value5=Entry(F2,width=10,textvariable=self.x_value5,font=('times new romen',16,'bold'),relief=SUNKEN).grid(row=4,column=1,padx=10,pady=2)
        
        x_value6=Label(F2,text='X6',font=('times new romen',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=5,column=0,padx=1,pady=1,sticky='w')
        x_value6=Entry(F2,width=10,textvariable=self.x_value6,font=('times new romen',16,'bold'),relief=SUNKEN).grid(row=5,column=1,padx=10,pady=2)
        
        x_value7=Label(F2,text='X7',font=('times new romen',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=6,column=0,padx=1,pady=1,sticky='w')
        x_value7=Entry(F2,width=10,textvariable=self.x_value7,font=('times new romen',16,'bold'),relief=SUNKEN).grid(row=6,column=1,padx=10,pady=2)
        
        x_value8=Label(F2,text='X8',font=('times new romen',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=7,column=0,padx=1,pady=1,sticky='w')
        x_value8=Entry(F2,width=10,textvariable=self.x_value8,font=('times new romen',16,'bold'),relief=SUNKEN).grid(row=7,column=1,padx=10,pady=2)
        
        x_value9=Label(F2,text='X9',font=('times new romen',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=8,column=0,padx=1,pady=1,sticky='w')
        x_value9=Entry(F2,width=10,textvariable=self.x_value9,font=('times new romen',16,'bold'),relief=SUNKEN).grid(row=8,column=1,padx=10,pady=2)
        
        x_value10=Label(F2,text='X10',font=('times new romen',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=9,column=0,padx=1,pady=1,sticky='w')
        x_value10=Entry(F2,width=10,textvariable=self.x_value10,font=('times new romen',16,'bold'),relief=SUNKEN).grid(row=9,column=1,padx=10,pady=2)
        
        x_value11=Label(F2,text='X11',font=('times new romen',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=10,column=0,padx=1,pady=1,sticky='w')
        x_value11=Entry(F2,width=10,textvariable=self.x_value11,font=('times new romen',16,'bold'),relief=SUNKEN).grid(row=10,column=1,padx=10,pady=2)
        
        x_value12=Label(F2,text='X12',font=('times new romen',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=11,column=0,padx=1,pady=1,sticky='w')
        x_value12=Entry(F2,width=10,textvariable=self.x_value12,font=('times new romen',16,'bold'),relief=SUNKEN).grid(row=11,column=1,padx=10,pady=2)
        
       
         ###################################################
        F3=LabelFrame(self.root,bd=3,relief=GROOVE,text="Enter X value",font=('Times new roman',15,'bold'),fg='gold',bg=bg_color)
        F3.place(x=200,y=150,width=200,height=400)
        
        y_value1=Label(F3,text='Y1',font=('times new romen',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=0,column=0,padx=6,pady=1,sticky='w')
        y_value1=Entry(F3,width=10,textvariable=self.y_value1,font=('times new romen',16,'bold'),relief=SUNKEN).grid(row=0,column=1,padx=10,pady=2)
        
        y_value2=Label(F3,text='Y2',font=('times new romen',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=1,column=0,padx=6,pady=1,sticky='w')
        y_value2=Entry(F3,width=10,textvariable=self.y_value2,font=('times new romen',16,'bold'),relief=SUNKEN).grid(row=1,column=1,padx=10,pady=2)
        
        y_value3=Label(F3,text='Y3',font=('times new romen',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=2,column=0,padx=6,pady=1,sticky='w')
        y_value3=Entry(F3,width=10,textvariable=self.y_value3,font=('times new romen',16,'bold'),relief=SUNKEN).grid(row=2,column=1,padx=10,pady=2)
        
        y_value4=Label(F3,text='Y4',font=('times new romen',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=3,column=0,padx=6,pady=1,sticky='w')
        y_value4=Entry(F3,width=10,textvariable=self.y_value4,font=('times new romen',16,'bold'),relief=SUNKEN).grid(row=3,column=1,padx=10,pady=2)
        
        y_value5=Label(F3,text='Y5',font=('times new romen',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=4,column=0,padx=6,pady=1,sticky='w')
        y_value5=Entry(F3,width=10,textvariable=self.y_value5,font=('times new romen',16,'bold'),relief=SUNKEN).grid(row=4,column=1,padx=10,pady=2)
        
        y_value6=Label(F3,text='Y6',font=('times new romen',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=5,column=0,padx=6,pady=1,sticky='w')
        y_value6=Entry(F3,width=10,textvariable=self.y_value6,font=('times new romen',16,'bold'),relief=SUNKEN).grid(row=5,column=1,padx=10,pady=2)
        
        y_value7=Label(F3,text='Y7',font=('times new romen',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=6,column=0,padx=6,pady=1,sticky='w')
        y_value7=Entry(F3,width=10,textvariable=self.y_value7,font=('times new romen',16,'bold'),relief=SUNKEN).grid(row=6,column=1,padx=10,pady=2)
        
        y_value8=Label(F3,text='Y8',font=('times new romen',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=7,column=0,padx=6,pady=1,sticky='w')
        y_value8=Entry(F3,width=10,textvariable=self.y_value8,font=('times new romen',16,'bold'),relief=SUNKEN).grid(row=7,column=1,padx=10,pady=2)
        
        y_value9=Label(F3,text='Y9',font=('times new romen',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=8,column=0,padx=6,pady=1,sticky='w')
        y_value9=Entry(F3,width=10,textvariable=self.y_value9,font=('times new romen',16,'bold'),relief=SUNKEN).grid(row=8,column=1,padx=10,pady=2)
        
        y_value10=Label(F3,text='Y10',font=('times new romen',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=9,column=0,padx=6,pady=1,sticky='w')
        y_value10=Entry(F3,width=10,textvariable=self.y_value10,font=('times new romen',16,'bold'),relief=SUNKEN).grid(row=9,column=1,padx=10,pady=2)
        
        y_value11=Label(F3,text='Y11',font=('times new romen',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=10,column=0,padx=6,pady=1,sticky='w')
        y_value11=Entry(F3,width=10,textvariable=self.y_value11,font=('times new romen',16,'bold'),relief=SUNKEN).grid(row=10,column=1,padx=10,pady=2)
        
        y_value12=Label(F3,text='Y12',font=('times new romen',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=11,column=0,padx=6,pady=1,sticky='w')
        y_value12=Entry(F3,width=10,textvariable=self.y_value12,font=('times new romen',16,'bold'),relief=SUNKEN).grid(row=11,column=1,padx=10,pady=2)
        
        
    
        #######################################
        self.cos_x_1=(math.cos((self.x_value1.get() *3.14)/180))
        self.cos_x_1
        
        ###############################################
        
        F4=Frame(root,bd=3,relief=GROOVE)
        F4.place(x=401,y=150,width=870,height=400)
        bill_title=Label(F4,text='PRACTICAL HARMONIC ANAYSIS TABEL',font='arial 15 bold',bd=3,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F4,orient=VERTICAL)
        scrol_x=Scrollbar(F4,orient=HORIZONTAL)
        
        self.txtarea=Text(F4,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        
        
        self.txtarea.insert(END,"\t\t\t\t\tPRACTICAL HORMONIC ANAYSIS \n\n\n")
       
        
        scrol_y.pack(side=RIGHT) 
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
    
            
        F5=LabelFrame(self.root,bd=3,relief=GROOVE,text="FINAL ANS OF PRACTICAL HARMONIC ANYSIS IS",font=('Times new roman',15,'bold'),fg='gold',bg=bg_color)
        F5.place(x=0,y=550,relwidth=1,height=110)
        
        y_value9=Label(F5,text='f(x)',font=('times new romen',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=6,column=0,padx=10,pady=10,sticky='w')
        y_value9=Entry(F5,textvariable=self.final_value1,bd=3,width=80,font=('times new romen',16,'bold'),relief=SUNKEN).grid(row=6,column=1,padx=10,pady=10)
        
        
        btn_F=Frame(F5,bd=3,relief=GROOVE)
        btn_F.place(x=1040,width=229,height=50)
        
        
        total_btn=Button(btn_F,text='Total',bg='cadetblue',fg='white',pady=2,padx=1,width=6,font='arial 12 bold').grid(row=0,column=0,padx=4,pady=6)
        GBill_btn=Button(btn_F,command=self.welcome_bill,text='Genrate',bg='cadetblue',fg='white',pady=1,padx=1,width=6,font='arial 12 bold').grid(row=0,column=1,padx=4,pady=6)
        clear=Button(btn_F,text='Save:',command=self.save_bill,bg='cadetblue',fg='white',pady=1,padx=1,width=5,font='arial 12 bold').grid(row=0,column=2,padx=4,pady=6)
        self.welcome_bill()
         
    
    def welcome_bill(self):
        if self.hormonics.get()==1:
            if(self.x_value.get()==6):
                x_value_num=[]
                y_value_num=[]
                y_sin_x_num=[]
                y_cos_x_num=[]
            
                self.final_value.set(float(
                            (float(self.y_value1.get()))+
                            (float(self.y_value2.get()))+
                            (float(self.y_value3.get()))+
                            (float(self.y_value4.get()))+
                            (float(self.y_value5.get()))+
                            (float(self.y_value6.get()))
                            )
                            )  
                self.txtarea.delete('1.0',END)
                self.txtarea.insert(END,'\t\t\t\t\tPractical Hormonic Analysis')
                self.txtarea.insert(END,f"\nNumber of X value is:------->{self.x_value.get()}")
                self.txtarea.insert(END,f"\nNumber of Y value:---------->{self.y_value.get()}")
                self.txtarea.insert(END,f"\nNumber of Hormonic value:--->{self.hormonics.get()}")
                self.txtarea.insert(END,'\n\n*************************************************************************************************')
                self.txtarea.insert(END,"\nsin(x)\t\tcos(x)\t\tysin(x)\t\tycos(x)")
                self.txtarea.insert(END,'\n*************************************************************************************************')
        
                sin_x_1=round(float(math.sin((self.x_value1.get()*3.14)/180)),3)
                x_value_num.append(sin_x_1)
                sin_x_2=round(float(math.sin((self.x_value2.get()*3.14)/180)),3)
                x_value_num.append(sin_x_2)
                sin_x_3=round(float(math.sin((self.x_value3.get()*3.14)/180)),3)
                x_value_num.append(sin_x_3)
                sin_x_4=round(float(math.sin((self.x_value4.get()*3.14)/180)),3)
                x_value_num.append(sin_x_4)
                sin_x_5=round(float(math.sin((self.x_value5.get()*3.14)/180)),3)
                x_value_num.append(sin_x_5)
                sin_x_6=round(float(math.sin((self.x_value6.get()*3.14)/180)),3)
                x_value_num.append(sin_x_6)
            
                cos_x_1=round(float(math.cos((self.x_value1.get()*3.14)/180)),3)
                y_value_num.append(cos_x_1)
                cos_x_2=round(float(math.cos((self.x_value2.get()*3.14)/180)),3)
                y_value_num.append(cos_x_2)
                cos_x_3=round(float(math.cos((self.x_value3.get()*3.14)/180)),3)
                y_value_num.append(cos_x_3)
                cos_x_4=round(float(math.cos((self.x_value4.get()*3.14)/180)),3)
                y_value_num.append(cos_x_4)
                cos_x_5=round(float(math.cos((self.x_value5.get()*3.14)/180)),3)
                y_value_num.append(cos_x_5)
                cos_x_6=round(float(math.cos((self.x_value6.get()*3.14)/180)),3)
                y_value_num.append(cos_x_6)
            
        
                y_sin_x_1=round(float(float(self.y_value1.get()) * sin_x_1),3)
                y_sin_x_num.append(y_sin_x_1)
                y_sin_x_2=round(float(float(self.y_value2.get()) * sin_x_2),3)
                y_sin_x_num.append(y_sin_x_2)
                y_sin_x_3=round(float(float(self.y_value3.get()) * sin_x_3),3)
                y_sin_x_num.append(y_sin_x_3)
                y_sin_x_4=round(float(float(self.y_value4.get()) * sin_x_4),3)
                y_sin_x_num.append(y_sin_x_4)
                y_sin_x_5=round(float(float(self.y_value5.get()) * sin_x_5),3)
                y_sin_x_num.append(y_sin_x_5)
                y_sin_x_6=round(float(float(self.y_value6.get()) * sin_x_6),3)
                y_sin_x_num.append(y_sin_x_6)

                y_cos_x_1=round(float(float(self.y_value1.get()) * cos_x_1),3)
                y_cos_x_num.append(y_cos_x_1)
                y_cos_x_2=round(float(float(self.y_value2.get()) * cos_x_2),3)
                y_cos_x_num.append(y_cos_x_2)
                y_cos_x_3=round(float(float(self.y_value3.get()) * cos_x_3),3)
                y_cos_x_num.append(y_cos_x_3)
                y_cos_x_4=round(float(float(self.y_value4.get()) * cos_x_4),3)
                y_cos_x_num.append(y_cos_x_4)
                y_cos_x_5=round(float(float(self.y_value5.get()) * cos_x_5),3)
                y_cos_x_num.append(y_cos_x_5)
                y_cos_x_6=round(float(float(self.y_value6.get()) * cos_x_6),3)
                y_cos_x_num.append(y_cos_x_6)
  
                y_cos_x_sum=y_cos_x_1 + y_cos_x_2 + y_cos_x_3 + y_cos_x_4 + y_cos_x_5 + y_cos_x_6
                y_sin_x_sum=y_sin_x_1 + y_sin_x_2 + y_sin_x_3 + y_sin_x_4 + y_sin_x_5 + y_sin_x_6 
            
                for i in range(6):
                    self.txtarea.insert(END,f'\n{x_value_num[i]}\t\t{y_value_num[i]}\t\t{y_sin_x_num[i]}\t\t{y_cos_x_num[i]}')

                self.txtarea.insert(END,'\n*************************************************************************************************\n')
                self.txtarea.insert(END,f'\nThe sum of the y is -------->{self.final_value.get()}')
                self.txtarea.insert(END,f"\nThe sum of the ycos(x):----->{y_cos_x_sum}")
                self.txtarea.insert(END,f"\nThe sum of the ysin(x):----->{y_sin_x_sum}")
                self.txtarea.insert(END,'\n*************************************************************************************************')
            
                self.txtarea.insert(END,'\n*************************************************************************************************\n')
                a=float(float(2/self.x_value.get()) *float(self.final_value.get()))
                a0=a/2
                a1=float(float(2/self.x_value.get()) *float(y_cos_x_sum))
                b1=float(float(2/self.x_value.get()) *float(y_sin_x_sum))
                self.txtarea.insert(END,f'\na0 is:------->{a0}')
                self.txtarea.insert(END,f"\na1 is:------->{a1}")
                self.txtarea.insert(END,f"\nb1 is:------->{b1}")
                self.txtarea.insert(END,'\n*************************************************************************************************')
                self.save_bill()
        
        #######################for 2nd hormonic anysis########################
            if(self.x_value.get()==7):
                x_value_num=[]
                y_value_num=[]
                y_sin_x_num=[]
                y_cos_x_num=[]

                self.final_value.set(float(
                            (float(self.y_value1.get()))+
                            (float(self.y_value2.get()))+
                            (float(self.y_value3.get()))+
                            (float(self.y_value4.get()))+
                            (float(self.y_value5.get()))+
                            (float(self.y_value6.get()))+
                            (float(self.y_value7.get()))
                            )
                            )  
            
                self.txtarea.delete('1.0',END)
                self.txtarea.insert(END,'\t\t\t\t\tPractical Hormonic Analysis')
                self.txtarea.insert(END,f"\nNumber of X value is:------->{self.x_value.get()}")
                self.txtarea.insert(END,f"\nNumber of Y value:---------->{self.y_value.get()}")
                self.txtarea.insert(END,f"\nNumber of Hormonic value:--->{self.hormonics.get()}")
                self.txtarea.insert(END,'\n\n*************************************************************************************************')
                self.txtarea.insert(END,"\nsin(x)\t\tcos(x)\t\tysin(x)\t\tycos(x)")
                self.txtarea.insert(END,'\n*************************************************************************************************')
        
                sin_x_1=round(float(math.sin((self.x_value1.get()*3.14)/180)),3)
                x_value_num.append(sin_x_1)
                sin_x_2=round(float(math.sin((self.x_value2.get()*3.14)/180)),3)
                x_value_num.append(sin_x_2)
                sin_x_3=round(float(math.sin((self.x_value3.get()*3.14)/180)),3)
                x_value_num.append(sin_x_3)
                sin_x_4=round(float(math.sin((self.x_value4.get()*3.14)/180)),3)
                x_value_num.append(sin_x_4)
                sin_x_5=round(float(math.sin((self.x_value5.get()*3.14)/180)),3)
                x_value_num.append(sin_x_5)
                sin_x_6=round(float(math.sin((self.x_value6.get()*3.14)/180)),3)
                x_value_num.append(sin_x_6)
                sin_x_7=round(float(math.sin((self.x_value7.get()*3.14)/180)),3)
                x_value_num.append(sin_x_7)
        
                cos_x_1=round(float(math.cos((self.x_value1.get()*3.14)/180)),3)
                y_value_num.append(cos_x_1)
                cos_x_2=round(float(math.cos((self.x_value2.get()*3.14)/180)),3)
                y_value_num.append(cos_x_2)
                cos_x_3=round(float(math.cos((self.x_value3.get()*3.14)/180)),3)
                y_value_num.append(cos_x_3)
                cos_x_4=round(float(math.cos((self.x_value4.get()*3.14)/180)),3)
                y_value_num.append(cos_x_4)
                cos_x_5=round(float(math.cos((self.x_value5.get()*3.14)/180)),3)
                y_value_num.append(cos_x_5)
                cos_x_6=round(float(math.cos((self.x_value6.get()*3.14)/180)),3)
                y_value_num.append(cos_x_6)
                cos_x_7=round(float(math.cos((self.x_value7.get()*3.14)/180)),3)
                y_value_num.append(cos_x_7)

                y_sin_x_1=round(float(float(self.y_value1.get()) * sin_x_1),3)
                y_sin_x_num.append(y_sin_x_1)
                y_sin_x_2=round(float(float(self.y_value2.get()) * sin_x_2),3)
                y_sin_x_num.append(y_sin_x_2)
                y_sin_x_3=round(float(float(self.y_value3.get()) * sin_x_3),3)
                y_sin_x_num.append(y_sin_x_3)
                y_sin_x_4=round(float(float(self.y_value4.get()) * sin_x_4),3)
                y_sin_x_num.append(y_sin_x_4)
                y_sin_x_5=round(float(float(self.y_value5.get()) * sin_x_5),3)
                y_sin_x_num.append(y_sin_x_5)
                y_sin_x_6=round(float(float(self.y_value6.get()) * sin_x_6),3)
                y_sin_x_num.append(y_sin_x_6)
                y_sin_x_7=round(float(float(self.y_value7.get()) * sin_x_7),3)
                y_sin_x_num.append(y_sin_x_7)
        
                y_cos_x_1=round(float(float(self.y_value1.get()) * cos_x_1),3)
                y_cos_x_num.append(y_cos_x_1)
                y_cos_x_2=round(float(float(self.y_value2.get()) * cos_x_2),3)
                y_cos_x_num.append(y_cos_x_2)
                y_cos_x_3=round(float(float(self.y_value3.get()) * cos_x_3),3)
                y_cos_x_num.append(y_cos_x_3)
                y_cos_x_4=round(float(float(self.y_value4.get()) * cos_x_4),3)
                y_cos_x_num.append(y_cos_x_4)
                y_cos_x_5=round(float(float(self.y_value5.get()) * cos_x_5),3)
                y_cos_x_num.append(y_cos_x_5)
                y_cos_x_6=round(float(float(self.y_value6.get()) * cos_x_6),3)
                y_cos_x_num.append(y_cos_x_6)
                y_cos_x_7=round(float(float(self.y_value7.get()) * cos_x_7),3)
                y_cos_x_num.append(y_cos_x_7)
        
        
                y_cos_x_sum=y_cos_x_1 + y_cos_x_2 + y_cos_x_3 + y_cos_x_4 + y_cos_x_5 + y_cos_x_6+ y_cos_x_6
                y_sin_x_sum=y_sin_x_1 + y_sin_x_2 + y_sin_x_3 + y_sin_x_4 + y_sin_x_5 + y_sin_x_6+ y_sin_x_7
           
                           
                for i in range(7):
                    self.txtarea.insert(END,f'\n{x_value_num[i]}\t\t{y_value_num[i]}\t\t{y_sin_x_num[i]}\t\t{y_cos_x_num[i]}')

                self.txtarea.insert(END,'\n*************************************************************************************************\n')
                self.txtarea.insert(END,f'\nThe sum of the y is -------->{self.final_value.get()}')
                self.txtarea.insert(END,f"\nThe sum of the ycos(x):----->{y_cos_x_sum}")
                self.txtarea.insert(END,f"\nThe sum of the ysin(x):----->{y_sin_x_sum}")
                self.txtarea.insert(END,'\n*************************************************************************************************')
            
                self.txtarea.insert(END,'\n*************************************************************************************************\n')
                a=float(float(2/self.x_value.get()) *float(self.final_value.get()))
                a0=a/2
                a1=float(float(2/self.x_value.get()) *float(y_cos_x_sum))
                b1=float(float(2/self.x_value.get()) *float(y_sin_x_sum))
                self.txtarea.insert(END,f'\na0 is:------->{a0}')
                self.txtarea.insert(END,f"\na1 is:------->{a1}")
                self.txtarea.insert(END,f"\nb1 is:------->{b1}")
                self.txtarea.insert(END,'\n*************************************************************************************************')
                self.save_bill()
            if(self.x_value.get()==8):
                x_value_num=[]
                y_value_num=[]
                y_sin_x_num=[]
                y_cos_x_num=[]

                self.final_value.set(float(
                            (float(self.y_value1.get()))+
                            (float(self.y_value2.get()))+
                            (float(self.y_value3.get()))+
                            (float(self.y_value4.get()))+
                            (float(self.y_value5.get()))+
                            (float(self.y_value6.get()))+
                            (float(self.y_value7.get()))+
                            (float(self.y_value8.get()))
                            )
                            )  
            
                self.txtarea.delete('1.0',END)
                self.txtarea.insert(END,'\t\t\t\t\tPractical Hormonic Analysis')
                self.txtarea.insert(END,f"\nNumber of X value is:------->{self.x_value.get()}")
                self.txtarea.insert(END,f"\nNumber of Y value:---------->{self.y_value.get()}")
                self.txtarea.insert(END,f"\nNumber of Hormonic value:--->{self.hormonics.get()}")
                self.txtarea.insert(END,'\n\n*************************************************************************************************')
                self.txtarea.insert(END,"\nsin(x)\t\tcos(x)\t\tysin(x)\t\tycos(x)")
                self.txtarea.insert(END,'\n*************************************************************************************************')
        
                sin_x_1=round(float(math.sin((self.x_value1.get()*3.14)/180)),3)
                x_value_num.append(sin_x_1)
                sin_x_2=round(float(math.sin((self.x_value2.get()*3.14)/180)),3)
                x_value_num.append(sin_x_2)
                sin_x_3=round(float(math.sin((self.x_value3.get()*3.14)/180)),3)
                x_value_num.append(sin_x_3)
                sin_x_4=round(float(math.sin((self.x_value4.get()*3.14)/180)),3)
                x_value_num.append(sin_x_4)
                sin_x_5=round(float(math.sin((self.x_value5.get()*3.14)/180)),3)
                x_value_num.append(sin_x_5)
                sin_x_6=round(float(math.sin((self.x_value6.get()*3.14)/180)),3)
                x_value_num.append(sin_x_6)
                sin_x_7=round(float(math.sin((self.x_value7.get()*3.14)/180)),3)
                x_value_num.append(sin_x_7)
                sin_x_8=round(float(math.sin((self.x_value8.get()*3.14)/180)),3)
                x_value_num.append(sin_x_8)
        
                cos_x_1=round(float(math.cos((self.x_value1.get()*3.14)/180)),3)
                y_value_num.append(cos_x_1)
                cos_x_2=round(float(math.cos((self.x_value2.get()*3.14)/180)),3)
                y_value_num.append(cos_x_2)
                cos_x_3=round(float(math.cos((self.x_value3.get()*3.14)/180)),3)
                y_value_num.append(cos_x_3)
                cos_x_4=round(float(math.cos((self.x_value4.get()*3.14)/180)),3)
                y_value_num.append(cos_x_4)
                cos_x_5=round(float(math.cos((self.x_value5.get()*3.14)/180)),3)
                y_value_num.append(cos_x_5)
                cos_x_6=round(float(math.cos((self.x_value6.get()*3.14)/180)),3)
                y_value_num.append(cos_x_6)
                cos_x_7=round(float(math.cos((self.x_value7.get()*3.14)/180)),3)
                y_value_num.append(cos_x_7)
                cos_x_8=round(float(math.cos((self.x_value8.get()*3.14)/180)),3)
                y_value_num.append(cos_x_8)

                y_sin_x_1=round(float(float(self.y_value1.get()) * sin_x_1),3)
                y_sin_x_num.append(y_sin_x_1)
                y_sin_x_2=round(float(float(self.y_value2.get()) * sin_x_2),3)
                y_sin_x_num.append(y_sin_x_2)
                y_sin_x_3=round(float(float(self.y_value3.get()) * sin_x_3),3)
                y_sin_x_num.append(y_sin_x_3)
                y_sin_x_4=round(float(float(self.y_value4.get()) * sin_x_4),3)
                y_sin_x_num.append(y_sin_x_4)
                y_sin_x_5=round(float(float(self.y_value5.get()) * sin_x_5),3)
                y_sin_x_num.append(y_sin_x_5)
                y_sin_x_6=round(float(float(self.y_value6.get()) * sin_x_6),3)
                y_sin_x_num.append(y_sin_x_6)
                y_sin_x_7=round(float(float(self.y_value7.get()) * sin_x_7),3)
                y_sin_x_num.append(y_sin_x_7)
                y_sin_x_8=round(float(float(self.y_value8.get()) * sin_x_8),3)
                y_sin_x_num.append(y_sin_x_8)
        
                y_cos_x_1=round(float(float(self.y_value1.get()) * cos_x_1),3)
                y_cos_x_num.append(y_cos_x_1)
                y_cos_x_2=round(float(float(self.y_value2.get()) * cos_x_2),3)
                y_cos_x_num.append(y_cos_x_2)
                y_cos_x_3=round(float(float(self.y_value3.get()) * cos_x_3),3)
                y_cos_x_num.append(y_cos_x_3)
                y_cos_x_4=round(float(float(self.y_value4.get()) * cos_x_4),3)
                y_cos_x_num.append(y_cos_x_4)
                y_cos_x_5=round(float(float(self.y_value5.get()) * cos_x_5),3)
                y_cos_x_num.append(y_cos_x_5)
                y_cos_x_6=round(float(float(self.y_value6.get()) * cos_x_6),3)
                y_cos_x_num.append(y_cos_x_6)
                y_cos_x_7=round(float(float(self.y_value7.get()) * cos_x_7),3)
                y_cos_x_num.append(y_cos_x_7)
                y_cos_x_8=round(float(float(self.y_value8.get()) * cos_x_8),3)
                y_cos_x_num.append(y_cos_x_8)
        
        
                y_cos_x_sum=y_cos_x_1 + y_cos_x_2 + y_cos_x_3 + y_cos_x_4 + y_cos_x_5 + y_cos_x_6+ y_cos_x_7+ y_cos_x_8
                y_sin_x_sum=y_sin_x_1 + y_sin_x_2 + y_sin_x_3 + y_sin_x_4 + y_sin_x_5 + y_sin_x_6+ y_sin_x_7+ y_sin_x_8
           
                           
                for i in range(8):
                    self.txtarea.insert(END,f'\n{x_value_num[i]}\t\t{y_value_num[i]}\t\t{y_sin_x_num[i]}\t\t{y_cos_x_num[i]}')

                self.txtarea.insert(END,'\n*************************************************************************************************\n')
                self.txtarea.insert(END,f'\nThe sum of the y is -------->{self.final_value.get()}')
                self.txtarea.insert(END,f"\nThe sum of the ycos(x):----->{y_cos_x_sum}")
                self.txtarea.insert(END,f"\nThe sum of the ysin(x):----->{y_sin_x_sum}")
                self.txtarea.insert(END,'\n*************************************************************************************************')
            
                self.txtarea.insert(END,'\n*************************************************************************************************\n')
                a=float(float(2/self.x_value.get()) *float(self.final_value.get()))
                a0=a/2
                a1=float(float(2/self.x_value.get()) *float(y_cos_x_sum))
                b1=float(float(2/self.x_value.get()) *float(y_sin_x_sum))
                self.txtarea.insert(END,f'\na0 is:------->{a0}')
                self.txtarea.insert(END,f"\na1 is:------->{a1}")
                self.txtarea.insert(END,f"\nb1 is:------->{b1}")
                self.txtarea.insert(END,'\n*************************************************************************************************')
                self.save_bill()
            
                
                
            if(self.x_value.get()==9):
                x_value_num=[]
                y_value_num=[]
                y_sin_x_num=[]
                y_cos_x_num=[]

                self.final_value.set(float(
                            (float(self.y_value1.get()))+
                            (float(self.y_value2.get()))+
                            (float(self.y_value3.get()))+
                            (float(self.y_value4.get()))+
                            (float(self.y_value5.get()))+
                            (float(self.y_value6.get()))+
                            (float(self.y_value7.get()))+
                            (float(self.y_value8.get()))+
                            (float(self.y_value9.get()))
                             )
                            )  
                self.txtarea.delete('1.0',END)
                self.txtarea.insert(END,'\t\t\t\t\tPractical Hormonic Analysis')
                self.txtarea.insert(END,f"\nNumber of X value is:------->{self.x_value.get()}")
                self.txtarea.insert(END,f"\nNumber of Y value:---------->{self.y_value.get()}")
                self.txtarea.insert(END,f"\nNumber of Hormonic value:--->{self.hormonics.get()}")
                self.txtarea.insert(END,'\n\n*************************************************************************************************')
                self.txtarea.insert(END,"\nsin(x)\t\tcos(x)\t\tysin(x)\t\tycos(x)")
                self.txtarea.insert(END,'\n*************************************************************************************************')
        
                sin_x_1=round(float(math.sin((self.x_value1.get()*3.14)/180)),3)
                x_value_num.append(sin_x_1)
                sin_x_2=round(float(math.sin((self.x_value2.get()*3.14)/180)),3)
                x_value_num.append(sin_x_2)
                sin_x_3=round(float(math.sin((self.x_value3.get()*3.14)/180)),3)
                x_value_num.append(sin_x_3)
                sin_x_4=round(float(math.sin((self.x_value4.get()*3.14)/180)),3)
                x_value_num.append(sin_x_4)
                sin_x_5=round(float(math.sin((self.x_value5.get()*3.14)/180)),3)
                x_value_num.append(sin_x_5)
                sin_x_6=round(float(math.sin((self.x_value6.get()*3.14)/180)),3)
                x_value_num.append(sin_x_6)
                sin_x_7=round(float(math.sin((self.x_value7.get()*3.14)/180)),3)
                x_value_num.append(sin_x_7)
                sin_x_8=round(float(math.sin((self.x_value7.get()*3.14)/180)),3)
                x_value_num.append(sin_x_8)
                sin_x_9=round(float(math.sin((self.x_value9.get()*3.14)/180)),3)
                x_value_num.append(sin_x_9)
        
                cos_x_1=round(float(math.cos((self.x_value1.get()*3.14)/180)),3)
                y_value_num.append(cos_x_1)
                cos_x_2=round(float(math.cos((self.x_value2.get()*3.14)/180)),3)
                y_value_num.append(cos_x_2)
                cos_x_3=round(float(math.cos((self.x_value3.get()*3.14)/180)),3)
                y_value_num.append(cos_x_3)
                cos_x_4=round(float(math.cos((self.x_value4.get()*3.14)/180)),3)
                y_value_num.append(cos_x_4)
                cos_x_5=round(float(math.cos((self.x_value5.get()*3.14)/180)),3)
                y_value_num.append(cos_x_5)
                cos_x_6=round(float(math.cos((self.x_value6.get()*3.14)/180)),3)
                y_value_num.append(cos_x_6)
                cos_x_7=round(float(math.cos((self.x_value7.get()*3.14)/180)),3)
                y_value_num.append(cos_x_7)
                cos_x_8=round(float(math.cos((self.x_value8.get()*3.14)/180)),3)
                y_value_num.append(cos_x_8)
                cos_x_9=round(float(math.cos((self.x_value9.get()*3.14)/180)),3)
                y_value_num.append(cos_x_9)

                y_sin_x_1=round(float(float(self.y_value1.get()) * sin_x_1),3)
                y_sin_x_num.append(y_sin_x_1)
                y_sin_x_2=round(float(float(self.y_value2.get()) * sin_x_2),3)
                y_sin_x_num.append(y_sin_x_2)
                y_sin_x_3=round(float(float(self.y_value3.get()) * sin_x_3),3)
                y_sin_x_num.append(y_sin_x_3)
                y_sin_x_4=round(float(float(self.y_value4.get()) * sin_x_4),3)
                y_sin_x_num.append(y_sin_x_4)
                y_sin_x_5=round(float(float(self.y_value5.get()) * sin_x_5),3)
                y_sin_x_num.append(y_sin_x_5)
                y_sin_x_6=round(float(float(self.y_value6.get()) * sin_x_6),3)
                y_sin_x_num.append(y_sin_x_6)
                y_sin_x_7=round(float(float(self.y_value7.get()) * sin_x_7),3)
                y_sin_x_num.append(y_sin_x_7)
                y_sin_x_8=round(float(float(self.y_value8.get()) * sin_x_8),3)
                y_sin_x_num.append(y_sin_x_8)
                y_sin_x_9=round(float(float(self.y_value9.get()) * sin_x_9),3)
                y_sin_x_num.append(y_sin_x_9)
        
                y_cos_x_1=round(float(float(self.y_value1.get()) * cos_x_1),3)
                y_cos_x_num.append(y_cos_x_1)
                y_cos_x_2=round(float(float(self.y_value2.get()) * cos_x_2),3)
                y_cos_x_num.append(y_cos_x_2)
                y_cos_x_3=round(float(float(self.y_value3.get()) * cos_x_3),3)
                y_cos_x_num.append(y_cos_x_3)
                y_cos_x_4=round(float(float(self.y_value4.get()) * cos_x_4),3)
                y_cos_x_num.append(y_cos_x_4)
                y_cos_x_5=round(float(float(self.y_value5.get()) * cos_x_5),3)
                y_cos_x_num.append(y_cos_x_5)
                y_cos_x_6=round(float(float(self.y_value6.get()) * cos_x_6),3)
                y_cos_x_num.append(y_cos_x_6)
                y_cos_x_7=round(float(float(self.y_value7.get()) * cos_x_7),3)
                y_cos_x_num.append(y_cos_x_7)
                y_cos_x_8=round(float(float(self.y_value8.get()) * cos_x_8),3)
                y_cos_x_num.append(y_cos_x_8)
                y_cos_x_9=round(float(float(self.y_value9.get()) * cos_x_9),3)
                y_cos_x_num.append(y_cos_x_9)
        
        
                y_cos_x_sum=y_cos_x_1 + y_cos_x_2 + y_cos_x_3 + y_cos_x_4 + y_cos_x_5 + y_cos_x_6+ y_cos_x_7+ y_cos_x_8+ y_cos_x_9
                y_sin_x_sum=y_sin_x_1 + y_sin_x_2 + y_sin_x_3 + y_sin_x_4 + y_sin_x_5 + y_sin_x_6+ y_sin_x_7+ y_sin_x_8+ y_sin_x_9
           
                           
                for i in range(9):
                    self.txtarea.insert(END,f'\n{x_value_num[i]}\t\t{y_value_num[i]}\t\t{y_sin_x_num[i]}\t\t{y_cos_x_num[i]}')

                self.txtarea.insert(END,'\n*************************************************************************************************\n')
                self.txtarea.insert(END,f'\nThe sum of the y is -------->{self.final_value.get()}')
                self.txtarea.insert(END,f"\nThe sum of the ycos(x):----->{y_cos_x_sum}")
                self.txtarea.insert(END,f"\nThe sum of the ysin(x):----->{y_sin_x_sum}")
                self.txtarea.insert(END,'\n*************************************************************************************************')
            
                self.txtarea.insert(END,'\n*************************************************************************************************\n')
                a=float(float(2/self.x_value.get()) *float(self.final_value.get()))
                a0=a/2
                a1=float(float(2/self.x_value.get()) *float(y_cos_x_sum))
                b1=float(float(2/self.x_value.get()) *float(y_sin_x_sum))
                self.txtarea.insert(END,f'\na0 is:------->{a0}')
                self.txtarea.insert(END,f"\na1 is:------->{a1}")
                self.txtarea.insert(END,f"\nb1 is:------->{b1}")
                self.txtarea.insert(END,'\n*************************************************************************************************')
            if(self.x_value.get()==10):
                x_value_num=[]
                y_value_num=[]
                y_sin_x_num=[]
                y_cos_x_num=[]

                self.final_value.set(float(
                            (float(self.y_value1.get()))+
                            (float(self.y_value2.get()))+
                            (float(self.y_value3.get()))+
                            (float(self.y_value4.get()))+
                            (float(self.y_value5.get()))+
                            (float(self.y_value6.get()))+
                            (float(self.y_value7.get()))+
                            (float(self.y_value8.get()))+
                            (float(self.y_value9.get()))+
                            (float(self.y_value10.get()))
                             )
                            )  
                self.txtarea.delete('1.0',END)
                self.txtarea.insert(END,'\t\t\t\t\tPractical Hormonic Analysis')
                self.txtarea.insert(END,f"\nNumber of X value is:------->{self.x_value.get()}")
                self.txtarea.insert(END,f"\nNumber of Y value:---------->{self.y_value.get()}")
                self.txtarea.insert(END,f"\nNumber of Hormonic value:--->{self.hormonics.get()}")
                self.txtarea.insert(END,'\n\n*************************************************************************************************')
                self.txtarea.insert(END,"\nsin(x)\t\tcos(x)\t\tysin(x)\t\tycos(x)")
                self.txtarea.insert(END,'\n*************************************************************************************************')
        
                sin_x_1=round(float(math.sin((self.x_value1.get()*3.14)/180)),3)
                x_value_num.append(sin_x_1)
                sin_x_2=round(float(math.sin((self.x_value2.get()*3.14)/180)),3)
                x_value_num.append(sin_x_2)
                sin_x_3=round(float(math.sin((self.x_value3.get()*3.14)/180)),3)
                x_value_num.append(sin_x_3)
                sin_x_4=round(float(math.sin((self.x_value4.get()*3.14)/180)),3)
                x_value_num.append(sin_x_4)
                sin_x_5=round(float(math.sin((self.x_value5.get()*3.14)/180)),3)
                x_value_num.append(sin_x_5)
                sin_x_6=round(float(math.sin((self.x_value6.get()*3.14)/180)),3)
                x_value_num.append(sin_x_6)
                sin_x_7=round(float(math.sin((self.x_value7.get()*3.14)/180)),3)
                x_value_num.append(sin_x_7)
                sin_x_8=round(float(math.sin((self.x_value8.get()*3.14)/180)),3)
                x_value_num.append(sin_x_8)
                sin_x_9=round(float(math.sin((self.x_value9.get()*3.14)/180)),3)
                x_value_num.append(sin_x_9)
                sin_x_10=round(float(math.sin((self.x_value10.get()*3.14)/180)),3)
                x_value_num.append(sin_x_10)
        
                cos_x_1=round(float(math.cos((self.x_value1.get()*3.14)/180)),3)
                y_value_num.append(cos_x_1)
                cos_x_2=round(float(math.cos((self.x_value2.get()*3.14)/180)),3)
                y_value_num.append(cos_x_2)
                cos_x_3=round(float(math.cos((self.x_value3.get()*3.14)/180)),3)
                y_value_num.append(cos_x_3)
                cos_x_4=round(float(math.cos((self.x_value4.get()*3.14)/180)),3)
                y_value_num.append(cos_x_4)
                cos_x_5=round(float(math.cos((self.x_value5.get()*3.14)/180)),3)
                y_value_num.append(cos_x_5)
                cos_x_6=round(float(math.cos((self.x_value6.get()*3.14)/180)),3)
                y_value_num.append(cos_x_6)
                cos_x_7=round(float(math.cos((self.x_value7.get()*3.14)/180)),3)
                y_value_num.append(cos_x_7)
                cos_x_8=round(float(math.cos((self.x_value8.get()*3.14)/180)),3)
                y_value_num.append(cos_x_8)
                cos_x_9=round(float(math.cos((self.x_value9.get()*3.14)/180)),3)
                y_value_num.append(cos_x_9)
                cos_x_10=round(float(math.cos((self.x_value10.get()*3.14)/180)),3)
                y_value_num.append(cos_x_10)

                y_sin_x_1=round(float(float(self.y_value1.get()) * sin_x_1),3)
                y_sin_x_num.append(y_sin_x_1)
                y_sin_x_2=round(float(float(self.y_value2.get()) * sin_x_2),3)
                y_sin_x_num.append(y_sin_x_2)
                y_sin_x_3=round(float(float(self.y_value3.get()) * sin_x_3),3)
                y_sin_x_num.append(y_sin_x_3)
                y_sin_x_4=round(float(float(self.y_value4.get()) * sin_x_4),3)
                y_sin_x_num.append(y_sin_x_4)
                y_sin_x_5=round(float(float(self.y_value5.get()) * sin_x_5),3)
                y_sin_x_num.append(y_sin_x_5)
                y_sin_x_6=round(float(float(self.y_value6.get()) * sin_x_6),3)
                y_sin_x_num.append(y_sin_x_6)
                y_sin_x_7=round(float(float(self.y_value7.get()) * sin_x_7),3)
                y_sin_x_num.append(y_sin_x_7)
                y_sin_x_8=round(float(float(self.y_value8.get()) * sin_x_8),3)
                y_sin_x_num.append(y_sin_x_8)
                y_sin_x_9=round(float(float(self.y_value9.get()) * sin_x_9),3)
                y_sin_x_num.append(y_sin_x_9)
                y_sin_x_10=round(float(float(self.y_value10.get()) * sin_x_10),3)
                y_sin_x_num.append(y_sin_x_10)
        
                y_cos_x_1=round(float(float(self.y_value1.get()) * cos_x_1),3)
                y_cos_x_num.append(y_cos_x_1)
                y_cos_x_2=round(float(float(self.y_value2.get()) * cos_x_2),3)
                y_cos_x_num.append(y_cos_x_2)
                y_cos_x_3=round(float(float(self.y_value3.get()) * cos_x_3),3)
                y_cos_x_num.append(y_cos_x_3)
                y_cos_x_4=round(float(float(self.y_value4.get()) * cos_x_4),3)
                y_cos_x_num.append(y_cos_x_4)
                y_cos_x_5=round(float(float(self.y_value5.get()) * cos_x_5),3)
                y_cos_x_num.append(y_cos_x_5)
                y_cos_x_6=round(float(float(self.y_value6.get()) * cos_x_6),3)
                y_cos_x_num.append(y_cos_x_6)
                y_cos_x_7=round(float(float(self.y_value7.get()) * cos_x_7),3)
                y_cos_x_num.append(y_cos_x_7)
                y_cos_x_8=round(float(float(self.y_value8.get()) * cos_x_8),3)
                y_cos_x_num.append(y_cos_x_8)
                y_cos_x_9=round(float(float(self.y_value9.get()) * cos_x_9),3)
                y_cos_x_num.append(y_cos_x_9)
                y_cos_x_10=round(float(float(self.y_value10.get()) * cos_x_10),3)
                y_cos_x_num.append(y_cos_x_10)
        
        
                y_cos_x_sum=y_cos_x_1 + y_cos_x_2 + y_cos_x_3 + y_cos_x_4 + y_cos_x_5 + y_cos_x_6+ y_cos_x_7+ y_cos_x_8+ y_cos_x_9+ y_cos_x_10
                y_sin_x_sum=y_sin_x_1 + y_sin_x_2 + y_sin_x_3 + y_sin_x_4 + y_sin_x_5 + y_sin_x_6+ y_sin_x_7+ y_sin_x_8+ y_sin_x_9+ y_sin_x_10
           
                           
                for i in range(10):
                    self.txtarea.insert(END,f'\n{x_value_num[i]}\t\t{y_value_num[i]}\t\t{y_sin_x_num[i]}\t\t{y_cos_x_num[i]}')

                self.txtarea.insert(END,'\n*************************************************************************************************\n')
                self.txtarea.insert(END,f'\nThe sum of the y is -------->{self.final_value.get()}')
                self.txtarea.insert(END,f"\nThe sum of the ycos(x):----->{y_cos_x_sum}")
                self.txtarea.insert(END,f"\nThe sum of the ysin(x):----->{y_sin_x_sum}")
                self.txtarea.insert(END,'\n*************************************************************************************************')
            
                self.txtarea.insert(END,'\n*************************************************************************************************\n')
                a=float(float(2/self.x_value.get()) *float(self.final_value.get()))
                a0=a/2
                a1=float(float(2/self.x_value.get()) *float(y_cos_x_sum))
                b1=float(float(2/self.x_value.get()) *float(y_sin_x_sum))
                self.txtarea.insert(END,f'\na0 is:------->{a0}')
                self.txtarea.insert(END,f"\na1 is:------->{a1}")
                self.txtarea.insert(END,f"\nb1 is:------->{b1}")
                self.txtarea.insert(END,'\n*************************************************************************************************')
            if(self.x_value.get()==11):
                x_value_num=[]
                y_value_num=[]
                y_sin_x_num=[]
                y_cos_x_num=[]

                self.final_value.set(float(
                            (float(self.y_value1.get()))+
                            (float(self.y_value2.get()))+
                            (float(self.y_value3.get()))+
                            (float(self.y_value4.get()))+
                            (float(self.y_value5.get()))+
                            (float(self.y_value6.get()))+
                            (float(self.y_value7.get()))+
                            (float(self.y_value8.get()))+
                            (float(self.y_value9.get()))+
                            (float(self.y_value10.get()))+
                            (float(self.y_value11.get()))
                             )
                            )  
                self.txtarea.delete('1.0',END)
                self.txtarea.insert(END,'\t\t\t\t\tPractical Hormonic Analysis')
                self.txtarea.insert(END,f"\nNumber of X value is:------->{self.x_value.get()}")
                self.txtarea.insert(END,f"\nNumber of Y value:---------->{self.y_value.get()}")
                self.txtarea.insert(END,f"\nNumber of Hormonic value:--->{self.hormonics.get()}")
                self.txtarea.insert(END,'\n\n*************************************************************************************************')
                self.txtarea.insert(END,"\nsin(x)\t\tcos(x)\t\tysin(x)\t\tycos(x)")
                self.txtarea.insert(END,'\n*************************************************************************************************')
        
                sin_x_1=round(float(math.sin((self.x_value1.get()*3.14)/180)),3)
                x_value_num.append(sin_x_1)
                sin_x_2=round(float(math.sin((self.x_value2.get()*3.14)/180)),3)
                x_value_num.append(sin_x_2)
                sin_x_3=round(float(math.sin((self.x_value3.get()*3.14)/180)),3)
                x_value_num.append(sin_x_3)
                sin_x_4=round(float(math.sin((self.x_value4.get()*3.14)/180)),3)
                x_value_num.append(sin_x_4)
                sin_x_5=round(float(math.sin((self.x_value5.get()*3.14)/180)),3)
                x_value_num.append(sin_x_5)
                sin_x_6=round(float(math.sin((self.x_value6.get()*3.14)/180)),3)
                x_value_num.append(sin_x_6)
                sin_x_7=round(float(math.sin((self.x_value7.get()*3.14)/180)),3)
                x_value_num.append(sin_x_7)
                sin_x_8=round(float(math.sin((self.x_value8.get()*3.14)/180)),3)
                x_value_num.append(sin_x_8)
                sin_x_9=round(float(math.sin((self.x_value9.get()*3.14)/180)),3)
                x_value_num.append(sin_x_9)
                sin_x_10=round(float(math.sin((self.x_value10.get()*3.14)/180)),3)
                x_value_num.append(sin_x_10)
                sin_x_11=round(float(math.sin((self.x_value11.get()*3.14)/180)),3)
                x_value_num.append(sin_x_11)
        
                cos_x_1=round(float(math.cos((self.x_value1.get()*3.14)/180)),3)
                y_value_num.append(cos_x_1)
                cos_x_2=round(float(math.cos((self.x_value2.get()*3.14)/180)),3)
                y_value_num.append(cos_x_2)
                cos_x_3=round(float(math.cos((self.x_value3.get()*3.14)/180)),3)
                y_value_num.append(cos_x_3)
                cos_x_4=round(float(math.cos((self.x_value4.get()*3.14)/180)),3)
                y_value_num.append(cos_x_4)
                cos_x_5=round(float(math.cos((self.x_value5.get()*3.14)/180)),3)
                y_value_num.append(cos_x_5)
                cos_x_6=round(float(math.cos((self.x_value6.get()*3.14)/180)),3)
                y_value_num.append(cos_x_6)
                cos_x_7=round(float(math.cos((self.x_value7.get()*3.14)/180)),3)
                y_value_num.append(cos_x_7)
                cos_x_8=round(float(math.cos((self.x_value8.get()*3.14)/180)),3)
                y_value_num.append(cos_x_8)
                cos_x_9=round(float(math.cos((self.x_value9.get()*3.14)/180)),3)
                y_value_num.append(cos_x_9)
                cos_x_10=round(float(math.cos((self.x_value10.get()*3.14)/180)),3)
                y_value_num.append(cos_x_10)
                cos_x_11=round(float(math.cos((self.x_value11.get()*3.14)/180)),3)
                y_value_num.append(cos_x_11)

                y_sin_x_1=round(float(float(self.y_value1.get()) * sin_x_1),3)
                y_sin_x_num.append(y_sin_x_1)
                y_sin_x_2=round(float(float(self.y_value2.get()) * sin_x_2),3)
                y_sin_x_num.append(y_sin_x_2)
                y_sin_x_3=round(float(float(self.y_value3.get()) * sin_x_3),3)
                y_sin_x_num.append(y_sin_x_3)
                y_sin_x_4=round(float(float(self.y_value4.get()) * sin_x_4),3)
                y_sin_x_num.append(y_sin_x_4)
                y_sin_x_5=round(float(float(self.y_value5.get()) * sin_x_5),3)
                y_sin_x_num.append(y_sin_x_5)
                y_sin_x_6=round(float(float(self.y_value6.get()) * sin_x_6),3)
                y_sin_x_num.append(y_sin_x_6)
                y_sin_x_7=round(float(float(self.y_value7.get()) * sin_x_7),3)
                y_sin_x_num.append(y_sin_x_7)
                y_sin_x_8=round(float(float(self.y_value8.get()) * sin_x_8),3)
                y_sin_x_num.append(y_sin_x_8)
                y_sin_x_9=round(float(float(self.y_value9.get()) * sin_x_9),3)
                y_sin_x_num.append(y_sin_x_9)
                y_sin_x_10=round(float(float(self.y_value10.get()) * sin_x_10),3)
                y_sin_x_num.append(y_sin_x_10)
                y_sin_x_11=round(float(float(self.y_value11.get()) * sin_x_11),3)
                y_sin_x_num.append(y_sin_x_11)
        
                y_cos_x_1=round(float(float(self.y_value1.get()) * cos_x_1),3)
                y_cos_x_num.append(y_cos_x_1)
                y_cos_x_2=round(float(float(self.y_value2.get()) * cos_x_2),3)
                y_cos_x_num.append(y_cos_x_2)
                y_cos_x_3=round(float(float(self.y_value3.get()) * cos_x_3),3)
                y_cos_x_num.append(y_cos_x_3)
                y_cos_x_4=round(float(float(self.y_value4.get()) * cos_x_4),3)
                y_cos_x_num.append(y_cos_x_4)
                y_cos_x_5=round(float(float(self.y_value5.get()) * cos_x_5),3)
                y_cos_x_num.append(y_cos_x_5)
                y_cos_x_6=round(float(float(self.y_value6.get()) * cos_x_6),3)
                y_cos_x_num.append(y_cos_x_6)
                y_cos_x_7=round(float(float(self.y_value7.get()) * cos_x_7),3)
                y_cos_x_num.append(y_cos_x_7)
                y_cos_x_8=round(float(float(self.y_value8.get()) * cos_x_8),3)
                y_cos_x_num.append(y_cos_x_8)
                y_cos_x_9=round(float(float(self.y_value9.get()) * cos_x_9),3)
                y_cos_x_num.append(y_cos_x_9)
                y_cos_x_10=round(float(float(self.y_value10.get()) * cos_x_10),3)
                y_cos_x_num.append(y_cos_x_10)
                y_cos_x_11=round(float(float(self.y_value11.get()) * cos_x_11),3)
                y_cos_x_num.append(y_cos_x_11)
        
        
                y_cos_x_sum=y_cos_x_1 + y_cos_x_2 + y_cos_x_3 + y_cos_x_4 + y_cos_x_5 + y_cos_x_6+ y_cos_x_7+ y_cos_x_8+ y_cos_x_9+ y_cos_x_10+ y_cos_x_11
                y_sin_x_sum=y_sin_x_1 + y_sin_x_2 + y_sin_x_3 + y_sin_x_4 + y_sin_x_5 + y_sin_x_6+ y_sin_x_7+ y_sin_x_8+ y_sin_x_9+ y_sin_x_10+ y_sin_x_11
           
                           
                for i in range(11):
                    self.txtarea.insert(END,f'\n{x_value_num[i]}\t\t{y_value_num[i]}\t\t{y_sin_x_num[i]}\t\t{y_cos_x_num[i]}')

                self.txtarea.insert(END,'\n*************************************************************************************************\n')
                self.txtarea.insert(END,f'\nThe sum of the y is -------->{self.final_value.get()}')
                self.txtarea.insert(END,f"\nThe sum of the ycos(x):----->{y_cos_x_sum}")
                self.txtarea.insert(END,f"\nThe sum of the ysin(x):----->{y_sin_x_sum}")
                self.txtarea.insert(END,'\n*************************************************************************************************')
            
                self.txtarea.insert(END,'\n*************************************************************************************************\n')
                a=float(float(2/self.x_value.get()) *float(self.final_value.get()))
                a0=a/2
                a1=float(float(2/self.x_value.get()) *float(y_cos_x_sum))
                b1=float(float(2/self.x_value.get()) *float(y_sin_x_sum))
                self.txtarea.insert(END,f'\na0 is:------->{a0}')
                self.txtarea.insert(END,f"\na1 is:------->{a1}")
                self.txtarea.insert(END,f"\nb1 is:------->{b1}")
                self.txtarea.insert(END,'\n*************************************************************************************************')
            if(self.x_value.get()==12):
                x_value_num=[]
                y_value_num=[]
                y_sin_x_num=[]
                y_cos_x_num=[]

                self.final_value.set(float(
                            (float(self.y_value1.get()))+
                            (float(self.y_value2.get()))+
                            (float(self.y_value3.get()))+
                            (float(self.y_value4.get()))+
                            (float(self.y_value5.get()))+
                            (float(self.y_value6.get()))+
                            (float(self.y_value7.get()))+
                            (float(self.y_value8.get()))+
                            (float(self.y_value9.get()))+
                            (float(self.y_value10.get()))+
                            (float(self.y_value11.get()))
                            (float(self.y_value12.get()))
                             )
                            )  
                self.txtarea.delete('1.0',END)
                self.txtarea.insert(END,'\t\t\t\t\tPractical Hormonic Analysis')
                self.txtarea.insert(END,f"\nNumber of X value is:------->{self.x_value.get()}")
                self.txtarea.insert(END,f"\nNumber of Y value:---------->{self.y_value.get()}")
                self.txtarea.insert(END,f"\nNumber of Hormonic value:--->{self.hormonics.get()}")
                self.txtarea.insert(END,'\n\n*************************************************************************************************')
                self.txtarea.insert(END,"\nsin(x)\t\tcos(x)\t\tysin(x)\t\tycos(x)")
                self.txtarea.insert(END,'\n*************************************************************************************************')
        
                sin_x_1=round(float(math.sin((self.x_value1.get()*3.14)/180)),3)
                x_value_num.append(sin_x_1)
                sin_x_2=round(float(math.sin((self.x_value2.get()*3.14)/180)),3)
                x_value_num.append(sin_x_2)
                sin_x_3=round(float(math.sin((self.x_value3.get()*3.14)/180)),3)
                x_value_num.append(sin_x_3)
                sin_x_4=round(float(math.sin((self.x_value4.get()*3.14)/180)),3)
                x_value_num.append(sin_x_4)
                sin_x_5=round(float(math.sin((self.x_value5.get()*3.14)/180)),3)
                x_value_num.append(sin_x_5)
                sin_x_6=round(float(math.sin((self.x_value6.get()*3.14)/180)),3)
                x_value_num.append(sin_x_6)
                sin_x_7=round(float(math.sin((self.x_value7.get()*3.14)/180)),3)
                x_value_num.append(sin_x_7)
                sin_x_8=round(float(math.sin((self.x_value8.get()*3.14)/180)),3)
                x_value_num.append(sin_x_8)
                sin_x_9=round(float(math.sin((self.x_value9.get()*3.14)/180)),3)
                x_value_num.append(sin_x_9)
                sin_x_10=round(float(math.sin((self.x_value10.get()*3.14)/180)),3)
                x_value_num.append(sin_x_10)
                sin_x_11=round(float(math.sin((self.x_value11.get()*3.14)/180)),3)
                x_value_num.append(sin_x_11)
                sin_x_12=round(float(math.sin((self.x_value12.get()*3.14)/180)),3)
                x_value_num.append(sin_x_12)
        
                cos_x_1=round(float(math.cos((self.x_value1.get()*3.14)/180)),3)
                y_value_num.append(cos_x_1)
                cos_x_2=round(float(math.cos((self.x_value2.get()*3.14)/180)),3)
                y_value_num.append(cos_x_2)
                cos_x_3=round(float(math.cos((self.x_value3.get()*3.14)/180)),3)
                y_value_num.append(cos_x_3)
                cos_x_4=round(float(math.cos((self.x_value4.get()*3.14)/180)),3)
                y_value_num.append(cos_x_4)
                cos_x_5=round(float(math.cos((self.x_value5.get()*3.14)/180)),3)
                y_value_num.append(cos_x_5)
                cos_x_6=round(float(math.cos((self.x_value6.get()*3.14)/180)),3)
                y_value_num.append(cos_x_6)
                cos_x_7=round(float(math.cos((self.x_value7.get()*3.14)/180)),3)
                y_value_num.append(cos_x_7)
                cos_x_8=round(float(math.cos((self.x_value8.get()*3.14)/180)),3)
                y_value_num.append(cos_x_8)
                cos_x_9=round(float(math.cos((self.x_value9.get()*3.14)/180)),3)
                y_value_num.append(cos_x_9)
                cos_x_10=round(float(math.cos((self.x_value10.get()*3.14)/180)),3)
                y_value_num.append(cos_x_10)
                cos_x_11=round(float(math.cos((self.x_value11.get()*3.14)/180)),3)
                y_value_num.append(cos_x_11)
                cos_x_12=round(float(math.cos((self.x_value12.get()*3.14)/180)),3)
                y_value_num.append(cos_x_12)

                y_sin_x_1=round(float(float(self.y_value1.get()) * sin_x_1),3)
                y_sin_x_num.append(y_sin_x_1)
                y_sin_x_2=round(float(float(self.y_value2.get()) * sin_x_2),3)
                y_sin_x_num.append(y_sin_x_2)
                y_sin_x_3=round(float(float(self.y_value3.get()) * sin_x_3),3)
                y_sin_x_num.append(y_sin_x_3)
                y_sin_x_4=round(float(float(self.y_value4.get()) * sin_x_4),3)
                y_sin_x_num.append(y_sin_x_4)
                y_sin_x_5=round(float(float(self.y_value5.get()) * sin_x_5),3)
                y_sin_x_num.append(y_sin_x_5)
                y_sin_x_6=round(float(float(self.y_value6.get()) * sin_x_6),3)
                y_sin_x_num.append(y_sin_x_6)
                y_sin_x_7=round(float(float(self.y_value7.get()) * sin_x_7),3)
                y_sin_x_num.append(y_sin_x_7)
                y_sin_x_8=round(float(float(self.y_value8.get()) * sin_x_8),3)
                y_sin_x_num.append(y_sin_x_8)
                y_sin_x_9=round(float(float(self.y_value9.get()) * sin_x_9),3)
                y_sin_x_num.append(y_sin_x_9)
                y_sin_x_10=round(float(float(self.y_value10.get()) * sin_x_10),3)
                y_sin_x_num.append(y_sin_x_10)
                y_sin_x_11=round(float(float(self.y_value11.get()) * sin_x_11),3)
                y_sin_x_num.append(y_sin_x_11)
                y_sin_x_12=round(float(float(self.y_value12.get()) * sin_x_12),3)
                y_sin_x_num.append(y_sin_x_12)
        
                y_cos_x_1=round(float(float(self.y_value1.get()) * cos_x_1),3)
                y_cos_x_num.append(y_cos_x_1)
                y_cos_x_2=round(float(float(self.y_value2.get()) * cos_x_2),3)
                y_cos_x_num.append(y_cos_x_2)
                y_cos_x_3=round(float(float(self.y_value3.get()) * cos_x_3),3)
                y_cos_x_num.append(y_cos_x_3)
                y_cos_x_4=round(float(float(self.y_value4.get()) * cos_x_4),3)
                y_cos_x_num.append(y_cos_x_4)
                y_cos_x_5=round(float(float(self.y_value5.get()) * cos_x_5),3)
                y_cos_x_num.append(y_cos_x_5)
                y_cos_x_6=round(float(float(self.y_value6.get()) * cos_x_6),3)
                y_cos_x_num.append(y_cos_x_6)
                y_cos_x_7=round(float(float(self.y_value7.get()) * cos_x_7),3)
                y_cos_x_num.append(y_cos_x_7)
                y_cos_x_8=round(float(float(self.y_value8.get()) * cos_x_8),3)
                y_cos_x_num.append(y_cos_x_8)
                y_cos_x_9=round(float(float(self.y_value9.get()) * cos_x_9),3)
                y_cos_x_num.append(y_cos_x_9)
                y_cos_x_10=round(float(float(self.y_value10.get()) * cos_x_10),3)
                y_cos_x_num.append(y_cos_x_10)
                y_cos_x_11=round(float(float(self.y_value11.get()) * cos_x_11),3)
                y_cos_x_num.append(y_cos_x_11)
                y_cos_x_12=round(float(float(self.y_value12.get()) * cos_x_12),3)
                y_cos_x_num.append(y_cos_x_12)
        
        
                y_cos_x_sum=y_cos_x_1 + y_cos_x_2 + y_cos_x_3 + y_cos_x_4 + y_cos_x_5 + y_cos_x_6+ y_cos_x_7+ y_cos_x_8+ y_cos_x_9+ y_cos_x_10+ y_cos_x_11+ y_cos_x_12
                y_sin_x_sum=y_sin_x_1 + y_sin_x_2 + y_sin_x_3 + y_sin_x_4 + y_sin_x_5 + y_sin_x_6+ y_sin_x_7+ y_sin_x_8+ y_sin_x_9+ y_sin_x_10+ y_sin_x_11+ y_sin_x_12
           
                           
                for i in range(12):
                    self.txtarea.insert(END,f'\n{x_value_num[i]}\t\t{y_value_num[i]}\t\t{y_sin_x_num[i]}\t\t{y_cos_x_num[i]}')

                self.txtarea.insert(END,'\n*************************************************************************************************\n')
                self.txtarea.insert(END,f'\nThe sum of the y is -------->{self.final_value.get()}')
                self.txtarea.insert(END,f"\nThe sum of the ycos(x):----->{y_cos_x_sum}")
                self.txtarea.insert(END,f"\nThe sum of the ysin(x):----->{y_sin_x_sum}")
                self.txtarea.insert(END,'\n*************************************************************************************************')
            
                self.txtarea.insert(END,'\n*************************************************************************************************\n')
                a=float(float(2/self.x_value.get()) *float(self.final_value.get()))
                a0=a/2
                a1=float(float(2/self.x_value.get()) *float(y_cos_x_sum))
                b1=float(float(2/self.x_value.get()) *float(y_sin_x_sum))
                self.txtarea.insert(END,f'\na0 is:------->{a0}')
                self.txtarea.insert(END,f"\na1 is:------->{a1}")
                self.txtarea.insert(END,f"\nb1 is:------->{b1}")
                self.txtarea.insert(END,'\n*************************************************************************************************')
            
        
        if self.hormonics.get()==2:
            if(self.x_value.get()==6):
                x_value_num=[]
                x_value2_num=[]
                y_value_num=[]
                y_value2_num=[]
                y_sin_x_num=[]
                y_sin_x2_num=[]
                y_cos_x_num=[]
                y_cos_x2_num=[]
            
                self.final_value.set(float(
                            (float(self.y_value1.get()))+
                            (float(self.y_value2.get()))+
                            (float(self.y_value3.get()))+
                            (float(self.y_value4.get()))+
                            (float(self.y_value5.get()))+
                            (float(self.y_value6.get()))
                            )
                            )  
                self.txtarea.delete('1.0',END)
                self.txtarea.insert(END,'\t\t\t\t\tPractical Hormonic Analysis')
                self.txtarea.insert(END,f"\nNumber of X value is:------->{self.x_value.get()}")
                self.txtarea.insert(END,f"\nNumber of Y value:---------->{self.y_value.get()}")
                self.txtarea.insert(END,f"\nNumber of Hormonic value:--->{self.hormonics.get()}")
                self.txtarea.insert(END,'\n\n*************************************************************************************************')
                self.txtarea.insert(END,"\nsin(x)\t\tcos(x)\t\tysin(x)\t\tycos(x)")
                self.txtarea.insert(END,'\n*************************************************************************************************')
        
                sin_x_1=round(float(math.sin((self.x_value1.get()*3.14)/180)),3)
                x_value_num.append(sin_x_1)
                sin_x_2=round(float(math.sin((self.x_value2.get()*3.14)/180)),3)
                x_value_num.append(sin_x_2)
                sin_x_3=round(float(math.sin((self.x_value3.get()*3.14)/180)),3)
                x_value_num.append(sin_x_3)
                sin_x_4=round(float(math.sin((self.x_value4.get()*3.14)/180)),3)
                x_value_num.append(sin_x_4)
                sin_x_5=round(float(math.sin((self.x_value5.get()*3.14)/180)),3)
                x_value_num.append(sin_x_5)
                sin_x_6=round(float(math.sin((self.x_value6.get()*3.14)/180)),3)
                x_value_num.append(sin_x_6)
                ################sin(2x)
                sin_2x_1=round(float(math.sin((2*self.x_value1.get()*3.14)/180)),3)
                x_value2_num.append(sin_2x_1)
                sin_2x_2=round(float(math.sin((2*self.x_value2.get()*3.14)/180)),3)
                x_value2_num.append(sin_2x_2)
                sin_2x_3=round(float(math.sin((2*self.x_value3.get()*3.14)/180)),3)
                x_value2_num.append(sin_2x_3)
                sin_2x_4=round(float(math.sin((2*self.x_value4.get()*3.14)/180)),3)
                x_value2_num.append(sin_2x_4)
                sin_2x_5=round(float(math.sin((2*self.x_value5.get()*3.14)/180)),3)
                x_value2_num.append(sin_2x_5)
                sin_2x_6=round(float(math.sin((2*self.x_value6.get()*3.14)/180)),3)
                x_value2_num.append(sin_2x_6)
            
                cos_x_1=round(float(math.cos((self.x_value1.get()*3.14)/180)),3)
                y_value_num.append(cos_x_1)
                cos_x_2=round(float(math.cos((self.x_value2.get()*3.14)/180)),3)
                y_value_num.append(cos_x_2)
                cos_x_3=round(float(math.cos((self.x_value3.get()*3.14)/180)),3)
                y_value_num.append(cos_x_3)
                cos_x_4=round(float(math.cos((self.x_value4.get()*3.14)/180)),3)
                y_value_num.append(cos_x_4)
                cos_x_5=round(float(math.cos((self.x_value5.get()*3.14)/180)),3)
                y_value_num.append(cos_x_5)
                cos_x_6=round(float(math.cos((self.x_value6.get()*3.14)/180)),3)
                y_value_num.append(cos_x_6)
                #########cos(2x)
                cos_2x_1=round(float(math.cos((self.x_value1.get()*3.14)/180)),3)
                y_value2_num.append(cos_2x_1)
                cos_2x_2=round(float(math.cos((self.x_value2.get()*3.14)/180)),3)
                y_value2_num.append(cos_2x_2)
                cos_2x_3=round(float(math.cos((self.x_value3.get()*3.14)/180)),3)
                y_value2_num.append(cos_2x_3)
                cos_2x_4=round(float(math.cos((self.x_value4.get()*3.14)/180)),3)
                y_value2_num.append(cos_2x_4)
                cos_2x_5=round(float(math.cos((self.x_value5.get()*3.14)/180)),3)
                y_value2_num.append(cos_2x_5)
                cos_2x_6=round(float(math.cos((self.x_value6.get()*3.14)/180)),3)
                y_value2_num.append(cos_2x_6)
            
        
                y_sin_x_1=round(float(float(self.y_value1.get()) * sin_x_1),3)
                y_sin_x_num.append(y_sin_x_1)
                y_sin_x_2=round(float(float(self.y_value2.get()) * sin_x_2),3)
                y_sin_x_num.append(y_sin_x_2)
                y_sin_x_3=round(float(float(self.y_value3.get()) * sin_x_3),3)
                y_sin_x_num.append(y_sin_x_3)
                y_sin_x_4=round(float(float(self.y_value4.get()) * sin_x_4),3)
                y_sin_x_num.append(y_sin_x_4)
                y_sin_x_5=round(float(float(self.y_value5.get()) * sin_x_5),3)
                y_sin_x_num.append(y_sin_x_5)
                y_sin_x_6=round(float(float(self.y_value6.get()) * sin_x_6),3)
                y_sin_x_num.append(y_sin_x_6)
                
                ########ysin(2x)
                y_sin_x2_1=round(float(float(self.y_value1.get()) * sin_2x_1),3)#####sin_2x_1
                y_sin_x2_num.append(y_sin_x2_1)
                y_sin_x2_2=round(float(float(self.y_value2.get()) * sin_2x_2),3)
                y_sin_x2_num.append(y_sin_x2_2)
                y_sin_x2_3=round(float(float(self.y_value3.get()) * sin_2x_3),3)
                y_sin_x2_num.append(y_sin_x2_3)
                y_sin_x2_4=round(float(float(self.y_value4.get()) * sin_2x_4),3)
                y_sin_x2_num.append(y_sin_x2_4)
                y_sin_x2_5=round(float(float(self.y_value5.get()) * sin_2x_5),3)
                y_sin_x2_num.append(y_sin_x2_5)
                y_sin_x2_6=round(float(float(self.y_value6.get()) * sin_2x_6),3)
                y_sin_x2_num.append(y_sin_x2_6)

                y_cos_x_1=round(float(float(self.y_value1.get()) * cos_x_1),3)
                y_cos_x_num.append(y_cos_x_1)
                y_cos_x_2=round(float(float(self.y_value2.get()) * cos_x_2),3)
                y_cos_x_num.append(y_cos_x_2)
                y_cos_x_3=round(float(float(self.y_value3.get()) * cos_x_3),3)
                y_cos_x_num.append(y_cos_x_3)
                y_cos_x_4=round(float(float(self.y_value4.get()) * cos_x_4),3)
                y_cos_x_num.append(y_cos_x_4)
                y_cos_x_5=round(float(float(self.y_value5.get()) * cos_x_5),3)
                y_cos_x_num.append(y_cos_x_5)
                y_cos_x_6=round(float(float(self.y_value6.get()) * cos_x_6),3)
                y_cos_x_num.append(y_cos_x_6)
                
                #######ycos(2x)
                y_cos_x2_1=round(float(float(self.y_value1.get()) * cos_2x_1),3)
                y_cos_x2_num.append(y_cos_x2_1)
                y_cos_x2_2=round(float(float(self.y_value2.get()) * cos_2x_2),3)
                y_cos_x2_num.append(y_cos_x2_2)
                y_cos_x2_3=round(float(float(self.y_value3.get()) * cos_2x_3),3)
                y_cos_x2_num.append(y_cos_x2_3)
                y_cos_x2_4=round(float(float(self.y_value4.get()) * cos_2x_4),3)
                y_cos_x2_num.append(y_cos_x2_4)
                y_cos_x2_5=round(float(float(self.y_value5.get()) * cos_2x_5),3)
                y_cos_x2_num.append(y_cos_x2_5)
                y_cos_x2_6=round(float(float(self.y_value6.get()) * cos_2x_6),3)
                y_cos_x2_num.append(y_cos_x2_6)
  
                y_cos_x_sum=y_cos_x_1 + y_cos_x_2 + y_cos_x_3 + y_cos_x_4 + y_cos_x_5 + y_cos_x_6
                y_sin_x_sum=y_sin_x_1 + y_sin_x_2 + y_sin_x_3 + y_sin_x_4 + y_sin_x_5 + y_sin_x_6 
                y_sin_x2_sum=y_sin_x2_1 + y_sin_x2_2 + y_sin_x2_3 + y_sin_x2_4 + y_sin_x2_5 + y_sin_x2_6
                for i in range(6):
                    self.txtarea.insert(END,f'\n{x_value_num[i]}\t\t{y_value_num[i]}\t\t{y_sin_x_num[i]}\t\t{y_cos_x_num[i]}\t\t{x_value2_num[i]}\t\t{y_value2_num[i]}\t\t{y_sin_x2_num[i]}\t\t{y_cos_x2_num[i]}')

                self.txtarea.insert(END,'\n*************************************************************************************************\n')
                self.txtarea.insert(END,f'\nThe sum of the y is -------->{self.final_value.get()}')
                self.txtarea.insert(END,f"\nThe sum of the ycos(x):----->{y_cos_x_sum}")
                self.txtarea.insert(END,f"\nThe sum of the ysin(x):----->{y_sin_x_sum}")
                self.txtarea.insert(END,'\n*************************************************************************************************')
            
                self.txtarea.insert(END,'\n*************************************************************************************************\n')
                a=float(float(2/self.x_value.get()) *float(self.final_value.get()))
                a0=a/2
                a1=float(float(2/self.x_value.get()) *float(y_cos_x_sum))
                b1=float(float(2/self.x_value.get()) *float(y_sin_x_sum))
                self.txtarea.insert(END,f'\na0 is:------->{a0}')
                self.txtarea.insert(END,f"\na1 is:------->{a1}")
                self.txtarea.insert(END,f"\nb1 is:------->{b1}")
                self.txtarea.insert(END,'\n*************************************************************************************************')
        
        
        #######################for 2nd hormonic anysis########################
            if(self.x_value.get()==7):
                x_value_num=[]
                y_value_num=[]
                y_sin_x_num=[]
                y_cos_x_num=[]

                self.final_value.set(float(
                            (float(self.y_value1.get()))+
                            (float(self.y_value2.get()))+
                            (float(self.y_value3.get()))+
                            (float(self.y_value4.get()))+
                            (float(self.y_value5.get()))+
                            (float(self.y_value6.get()))+
                            (float(self.y_value7.get()))
                            )
                            )  
            
                self.txtarea.delete('1.0',END)
                self.txtarea.insert(END,'\t\t\t\t\tPractical Hormonic Analysis')
                self.txtarea.insert(END,f"\nNumber of X value is:------->{self.x_value.get()}")
                self.txtarea.insert(END,f"\nNumber of Y value:---------->{self.y_value.get()}")
                self.txtarea.insert(END,f"\nNumber of Hormonic value:--->{self.hormonics.get()}")
                self.txtarea.insert(END,'\n\n*************************************************************************************************')
                self.txtarea.insert(END,"\nsin(x)\t\tcos(x)\t\tysin(x)\t\tycos(x)")
                self.txtarea.insert(END,'\n*************************************************************************************************')
        
                sin_x_1=round(float(math.sin((self.x_value1.get()*3.14)/180)),3)
                x_value_num.append(sin_x_1)
                sin_x_2=round(float(math.sin((self.x_value2.get()*3.14)/180)),3)
                x_value_num.append(sin_x_2)
                sin_x_3=round(float(math.sin((self.x_value3.get()*3.14)/180)),3)
                x_value_num.append(sin_x_3)
                sin_x_4=round(float(math.sin((self.x_value4.get()*3.14)/180)),3)
                x_value_num.append(sin_x_4)
                sin_x_5=round(float(math.sin((self.x_value5.get()*3.14)/180)),3)
                x_value_num.append(sin_x_5)
                sin_x_6=round(float(math.sin((self.x_value6.get()*3.14)/180)),3)
                x_value_num.append(sin_x_6)
                sin_x_7=round(float(math.sin((self.x_value7.get()*3.14)/180)),3)
                x_value_num.append(sin_x_7)
        
                cos_x_1=round(float(math.cos((self.x_value1.get()*3.14)/180)),3)
                y_value_num.append(cos_x_1)
                cos_x_2=round(float(math.cos((self.x_value2.get()*3.14)/180)),3)
                y_value_num.append(cos_x_2)
                cos_x_3=round(float(math.cos((self.x_value3.get()*3.14)/180)),3)
                y_value_num.append(cos_x_3)
                cos_x_4=round(float(math.cos((self.x_value4.get()*3.14)/180)),3)
                y_value_num.append(cos_x_4)
                cos_x_5=round(float(math.cos((self.x_value5.get()*3.14)/180)),3)
                y_value_num.append(cos_x_5)
                cos_x_6=round(float(math.cos((self.x_value6.get()*3.14)/180)),3)
                y_value_num.append(cos_x_6)
                cos_x_7=round(float(math.cos((self.x_value7.get()*3.14)/180)),3)
                y_value_num.append(cos_x_7)

                y_sin_x_1=round(float(float(self.y_value1.get()) * sin_x_1),3)
                y_sin_x_num.append(y_sin_x_1)
                y_sin_x_2=round(float(float(self.y_value2.get()) * sin_x_2),3)
                y_sin_x_num.append(y_sin_x_2)
                y_sin_x_3=round(float(float(self.y_value3.get()) * sin_x_3),3)
                y_sin_x_num.append(y_sin_x_3)
                y_sin_x_4=round(float(float(self.y_value4.get()) * sin_x_4),3)
                y_sin_x_num.append(y_sin_x_4)
                y_sin_x_5=round(float(float(self.y_value5.get()) * sin_x_5),3)
                y_sin_x_num.append(y_sin_x_5)
                y_sin_x_6=round(float(float(self.y_value6.get()) * sin_x_6),3)
                y_sin_x_num.append(y_sin_x_6)
                y_sin_x_7=round(float(float(self.y_value7.get()) * sin_x_7),3)
                y_sin_x_num.append(y_sin_x_7)
        
                y_cos_x_1=round(float(float(self.y_value1.get()) * cos_x_1),3)
                y_cos_x_num.append(y_cos_x_1)
                y_cos_x_2=round(float(float(self.y_value2.get()) * cos_x_2),3)
                y_cos_x_num.append(y_cos_x_2)
                y_cos_x_3=round(float(float(self.y_value3.get()) * cos_x_3),3)
                y_cos_x_num.append(y_cos_x_3)
                y_cos_x_4=round(float(float(self.y_value4.get()) * cos_x_4),3)
                y_cos_x_num.append(y_cos_x_4)
                y_cos_x_5=round(float(float(self.y_value5.get()) * cos_x_5),3)
                y_cos_x_num.append(y_cos_x_5)
                y_cos_x_6=round(float(float(self.y_value6.get()) * cos_x_6),3)
                y_cos_x_num.append(y_cos_x_6)
                y_cos_x_7=round(float(float(self.y_value7.get()) * cos_x_7),3)
                y_cos_x_num.append(y_cos_x_7)
        
        
                y_cos_x_sum=y_cos_x_1 + y_cos_x_2 + y_cos_x_3 + y_cos_x_4 + y_cos_x_5 + y_cos_x_6+ y_cos_x_6
                y_sin_x_sum=y_sin_x_1 + y_sin_x_2 + y_sin_x_3 + y_sin_x_4 + y_sin_x_5 + y_sin_x_6+ y_sin_x_7
           
                           
                for i in range(7):
                    self.txtarea.insert(END,f'\n{x_value_num[i]}\t\t{y_value_num[i]}\t\t{y_sin_x_num[i]}\t\t{y_cos_x_num[i]}')

                self.txtarea.insert(END,'\n*************************************************************************************************\n')
                self.txtarea.insert(END,f'\nThe sum of the y is -------->{self.final_value.get()}')
                self.txtarea.insert(END,f"\nThe sum of the ycos(x):----->{y_cos_x_sum}")
                self.txtarea.insert(END,f"\nThe sum of the ysin(x):----->{y_sin_x_sum}")
                self.txtarea.insert(END,'\n*************************************************************************************************')
            
                self.txtarea.insert(END,'\n*************************************************************************************************\n')
                a=float(float(2/self.x_value.get()) *float(self.final_value.get()))
                a0=a/2
                a1=float(float(2/self.x_value.get()) *float(y_cos_x_sum))
                b1=float(float(2/self.x_value.get()) *float(y_sin_x_sum))
                self.txtarea.insert(END,f'\na0 is:------->{a0}')
                self.txtarea.insert(END,f"\na1 is:------->{a1}")
                self.txtarea.insert(END,f"\nb1 is:------->{b1}")
                self.txtarea.insert(END,'\n*************************************************************************************************')
            if(self.x_value.get()==8):
                x_value_num=[]
                y_value_num=[]
                y_sin_x_num=[]
                y_cos_x_num=[]

                self.final_value.set(float(
                            (float(self.y_value1.get()))+
                            (float(self.y_value2.get()))+
                            (float(self.y_value3.get()))+
                            (float(self.y_value4.get()))+
                            (float(self.y_value5.get()))+
                            (float(self.y_value6.get()))+
                            (float(self.y_value7.get()))+
                            (float(self.y_value8.get()))
                            )
                            )  
            
                self.txtarea.delete('1.0',END)
                self.txtarea.insert(END,'\t\t\t\t\tPractical Hormonic Analysis')
                self.txtarea.insert(END,f"\nNumber of X value is:------->{self.x_value.get()}")
                self.txtarea.insert(END,f"\nNumber of Y value:---------->{self.y_value.get()}")
                self.txtarea.insert(END,f"\nNumber of Hormonic value:--->{self.hormonics.get()}")
                self.txtarea.insert(END,'\n\n*************************************************************************************************')
                self.txtarea.insert(END,"\nsin(x)\t\tcos(x)\t\tysin(x)\t\tycos(x)")
                self.txtarea.insert(END,'\n*************************************************************************************************')
        
                sin_x_1=round(float(math.sin((self.x_value1.get()*3.14)/180)),3)
                x_value_num.append(sin_x_1)
                sin_x_2=round(float(math.sin((self.x_value2.get()*3.14)/180)),3)
                x_value_num.append(sin_x_2)
                sin_x_3=round(float(math.sin((self.x_value3.get()*3.14)/180)),3)
                x_value_num.append(sin_x_3)
                sin_x_4=round(float(math.sin((self.x_value4.get()*3.14)/180)),3)
                x_value_num.append(sin_x_4)
                sin_x_5=round(float(math.sin((self.x_value5.get()*3.14)/180)),3)
                x_value_num.append(sin_x_5)
                sin_x_6=round(float(math.sin((self.x_value6.get()*3.14)/180)),3)
                x_value_num.append(sin_x_6)
                sin_x_7=round(float(math.sin((self.x_value7.get()*3.14)/180)),3)
                x_value_num.append(sin_x_7)
                sin_x_8=round(float(math.sin((self.x_value8.get()*3.14)/180)),3)
                x_value_num.append(sin_x_8)
        
                cos_x_1=round(float(math.cos((self.x_value1.get()*3.14)/180)),3)
                y_value_num.append(cos_x_1)
                cos_x_2=round(float(math.cos((self.x_value2.get()*3.14)/180)),3)
                y_value_num.append(cos_x_2)
                cos_x_3=round(float(math.cos((self.x_value3.get()*3.14)/180)),3)
                y_value_num.append(cos_x_3)
                cos_x_4=round(float(math.cos((self.x_value4.get()*3.14)/180)),3)
                y_value_num.append(cos_x_4)
                cos_x_5=round(float(math.cos((self.x_value5.get()*3.14)/180)),3)
                y_value_num.append(cos_x_5)
                cos_x_6=round(float(math.cos((self.x_value6.get()*3.14)/180)),3)
                y_value_num.append(cos_x_6)
                cos_x_7=round(float(math.cos((self.x_value7.get()*3.14)/180)),3)
                y_value_num.append(cos_x_7)
                cos_x_8=round(float(math.cos((self.x_value8.get()*3.14)/180)),3)
                y_value_num.append(cos_x_8)

                y_sin_x_1=round(float(float(self.y_value1.get()) * sin_x_1),3)
                y_sin_x_num.append(y_sin_x_1)
                y_sin_x_2=round(float(float(self.y_value2.get()) * sin_x_2),3)
                y_sin_x_num.append(y_sin_x_2)
                y_sin_x_3=round(float(float(self.y_value3.get()) * sin_x_3),3)
                y_sin_x_num.append(y_sin_x_3)
                y_sin_x_4=round(float(float(self.y_value4.get()) * sin_x_4),3)
                y_sin_x_num.append(y_sin_x_4)
                y_sin_x_5=round(float(float(self.y_value5.get()) * sin_x_5),3)
                y_sin_x_num.append(y_sin_x_5)
                y_sin_x_6=round(float(float(self.y_value6.get()) * sin_x_6),3)
                y_sin_x_num.append(y_sin_x_6)
                y_sin_x_7=round(float(float(self.y_value7.get()) * sin_x_7),3)
                y_sin_x_num.append(y_sin_x_7)
                y_sin_x_8=round(float(float(self.y_value8.get()) * sin_x_8),3)
                y_sin_x_num.append(y_sin_x_8)
        
                y_cos_x_1=round(float(float(self.y_value1.get()) * cos_x_1),3)
                y_cos_x_num.append(y_cos_x_1)
                y_cos_x_2=round(float(float(self.y_value2.get()) * cos_x_2),3)
                y_cos_x_num.append(y_cos_x_2)
                y_cos_x_3=round(float(float(self.y_value3.get()) * cos_x_3),3)
                y_cos_x_num.append(y_cos_x_3)
                y_cos_x_4=round(float(float(self.y_value4.get()) * cos_x_4),3)
                y_cos_x_num.append(y_cos_x_4)
                y_cos_x_5=round(float(float(self.y_value5.get()) * cos_x_5),3)
                y_cos_x_num.append(y_cos_x_5)
                y_cos_x_6=round(float(float(self.y_value6.get()) * cos_x_6),3)
                y_cos_x_num.append(y_cos_x_6)
                y_cos_x_7=round(float(float(self.y_value7.get()) * cos_x_7),3)
                y_cos_x_num.append(y_cos_x_7)
                y_cos_x_8=round(float(float(self.y_value8.get()) * cos_x_8),3)
                y_cos_x_num.append(y_cos_x_8)
        
        
                y_cos_x_sum=y_cos_x_1 + y_cos_x_2 + y_cos_x_3 + y_cos_x_4 + y_cos_x_5 + y_cos_x_6+ y_cos_x_7+ y_cos_x_8
                y_sin_x_sum=y_sin_x_1 + y_sin_x_2 + y_sin_x_3 + y_sin_x_4 + y_sin_x_5 + y_sin_x_6+ y_sin_x_7+ y_sin_x_8
           
                           
                for i in range(8):
                    self.txtarea.insert(END,f'\n{x_value_num[i]}\t\t{y_value_num[i]}\t\t{y_sin_x_num[i]}\t\t{y_cos_x_num[i]}')

                self.txtarea.insert(END,'\n*************************************************************************************************\n')
                self.txtarea.insert(END,f'\nThe sum of the y is -------->{self.final_value.get()}')
                self.txtarea.insert(END,f"\nThe sum of the ycos(x):----->{y_cos_x_sum}")
                self.txtarea.insert(END,f"\nThe sum of the ysin(x):----->{y_sin_x_sum}")
                self.txtarea.insert(END,'\n*************************************************************************************************')
            
                self.txtarea.insert(END,'\n*************************************************************************************************\n')
                a=float(float(2/self.x_value.get()) *float(self.final_value.get()))
                a0=a/2
                a1=float(float(2/self.x_value.get()) *float(y_cos_x_sum))
                b1=float(float(2/self.x_value.get()) *float(y_sin_x_sum))
                self.txtarea.insert(END,f'\na0 is:------->{a0}')
                self.txtarea.insert(END,f"\na1 is:------->{a1}")
                self.txtarea.insert(END,f"\nb1 is:------->{b1}")
                self.txtarea.insert(END,'\n*************************************************************************************************')
                
            if(self.x_value.get()==9):
                x_value_num=[]
                y_value_num=[]
                y_sin_x_num=[]
                y_cos_x_num=[]

                self.final_value.set(float(
                            (float(self.y_value1.get()))+
                            (float(self.y_value2.get()))+
                            (float(self.y_value3.get()))+
                            (float(self.y_value4.get()))+
                            (float(self.y_value5.get()))+
                            (float(self.y_value6.get()))+
                            (float(self.y_value7.get()))+
                            (float(self.y_value8.get()))+
                            (float(self.y_value9.get()))
                             )
                            )  
                self.txtarea.delete('1.0',END)
                self.txtarea.insert(END,'\t\t\t\t\tPractical Hormonic Analysis')
                self.txtarea.insert(END,f"\nNumber of X value is:------->{self.x_value.get()}")
                self.txtarea.insert(END,f"\nNumber of Y value:---------->{self.y_value.get()}")
                self.txtarea.insert(END,f"\nNumber of Hormonic value:--->{self.hormonics.get()}")
                self.txtarea.insert(END,'\n\n*************************************************************************************************')
                self.txtarea.insert(END,"\nsin(x)\t\tcos(x)\t\tysin(x)\t\tycos(x)")
                self.txtarea.insert(END,'\n*************************************************************************************************')
        
                sin_x_1=round(float(math.sin((self.x_value1.get()*3.14)/180)),3)
                x_value_num.append(sin_x_1)
                sin_x_2=round(float(math.sin((self.x_value2.get()*3.14)/180)),3)
                x_value_num.append(sin_x_2)
                sin_x_3=round(float(math.sin((self.x_value3.get()*3.14)/180)),3)
                x_value_num.append(sin_x_3)
                sin_x_4=round(float(math.sin((self.x_value4.get()*3.14)/180)),3)
                x_value_num.append(sin_x_4)
                sin_x_5=round(float(math.sin((self.x_value5.get()*3.14)/180)),3)
                x_value_num.append(sin_x_5)
                sin_x_6=round(float(math.sin((self.x_value6.get()*3.14)/180)),3)
                x_value_num.append(sin_x_6)
                sin_x_7=round(float(math.sin((self.x_value7.get()*3.14)/180)),3)
                x_value_num.append(sin_x_7)
                sin_x_8=round(float(math.sin((self.x_value7.get()*3.14)/180)),3)
                x_value_num.append(sin_x_8)
                sin_x_9=round(float(math.sin((self.x_value9.get()*3.14)/180)),3)
                x_value_num.append(sin_x_9)
        
                cos_x_1=round(float(math.cos((self.x_value1.get()*3.14)/180)),3)
                y_value_num.append(cos_x_1)
                cos_x_2=round(float(math.cos((self.x_value2.get()*3.14)/180)),3)
                y_value_num.append(cos_x_2)
                cos_x_3=round(float(math.cos((self.x_value3.get()*3.14)/180)),3)
                y_value_num.append(cos_x_3)
                cos_x_4=round(float(math.cos((self.x_value4.get()*3.14)/180)),3)
                y_value_num.append(cos_x_4)
                cos_x_5=round(float(math.cos((self.x_value5.get()*3.14)/180)),3)
                y_value_num.append(cos_x_5)
                cos_x_6=round(float(math.cos((self.x_value6.get()*3.14)/180)),3)
                y_value_num.append(cos_x_6)
                cos_x_7=round(float(math.cos((self.x_value7.get()*3.14)/180)),3)
                y_value_num.append(cos_x_7)
                cos_x_8=round(float(math.cos((self.x_value8.get()*3.14)/180)),3)
                y_value_num.append(cos_x_8)
                cos_x_9=round(float(math.cos((self.x_value9.get()*3.14)/180)),3)
                y_value_num.append(cos_x_9)

                y_sin_x_1=round(float(float(self.y_value1.get()) * sin_x_1),3)
                y_sin_x_num.append(y_sin_x_1)
                y_sin_x_2=round(float(float(self.y_value2.get()) * sin_x_2),3)
                y_sin_x_num.append(y_sin_x_2)
                y_sin_x_3=round(float(float(self.y_value3.get()) * sin_x_3),3)
                y_sin_x_num.append(y_sin_x_3)
                y_sin_x_4=round(float(float(self.y_value4.get()) * sin_x_4),3)
                y_sin_x_num.append(y_sin_x_4)
                y_sin_x_5=round(float(float(self.y_value5.get()) * sin_x_5),3)
                y_sin_x_num.append(y_sin_x_5)
                y_sin_x_6=round(float(float(self.y_value6.get()) * sin_x_6),3)
                y_sin_x_num.append(y_sin_x_6)
                y_sin_x_7=round(float(float(self.y_value7.get()) * sin_x_7),3)
                y_sin_x_num.append(y_sin_x_7)
                y_sin_x_8=round(float(float(self.y_value8.get()) * sin_x_8),3)
                y_sin_x_num.append(y_sin_x_8)
                y_sin_x_9=round(float(float(self.y_value9.get()) * sin_x_9),3)
                y_sin_x_num.append(y_sin_x_9)
        
                y_cos_x_1=round(float(float(self.y_value1.get()) * cos_x_1),3)
                y_cos_x_num.append(y_cos_x_1)
                y_cos_x_2=round(float(float(self.y_value2.get()) * cos_x_2),3)
                y_cos_x_num.append(y_cos_x_2)
                y_cos_x_3=round(float(float(self.y_value3.get()) * cos_x_3),3)
                y_cos_x_num.append(y_cos_x_3)
                y_cos_x_4=round(float(float(self.y_value4.get()) * cos_x_4),3)
                y_cos_x_num.append(y_cos_x_4)
                y_cos_x_5=round(float(float(self.y_value5.get()) * cos_x_5),3)
                y_cos_x_num.append(y_cos_x_5)
                y_cos_x_6=round(float(float(self.y_value6.get()) * cos_x_6),3)
                y_cos_x_num.append(y_cos_x_6)
                y_cos_x_7=round(float(float(self.y_value7.get()) * cos_x_7),3)
                y_cos_x_num.append(y_cos_x_7)
                y_cos_x_8=round(float(float(self.y_value8.get()) * cos_x_8),3)
                y_cos_x_num.append(y_cos_x_8)
                y_cos_x_9=round(float(float(self.y_value9.get()) * cos_x_9),3)
                y_cos_x_num.append(y_cos_x_9)
        
        
                y_cos_x_sum=y_cos_x_1 + y_cos_x_2 + y_cos_x_3 + y_cos_x_4 + y_cos_x_5 + y_cos_x_6+ y_cos_x_7+ y_cos_x_8+ y_cos_x_9
                y_sin_x_sum=y_sin_x_1 + y_sin_x_2 + y_sin_x_3 + y_sin_x_4 + y_sin_x_5 + y_sin_x_6+ y_sin_x_7+ y_sin_x_8+ y_sin_x_9
           
                           
                for i in range(9):
                    self.txtarea.insert(END,f'\n{x_value_num[i]}\t\t{y_value_num[i]}\t\t{y_sin_x_num[i]}\t\t{y_cos_x_num[i]}')

                self.txtarea.insert(END,'\n*************************************************************************************************\n')
                self.txtarea.insert(END,f'\nThe sum of the y is -------->{self.final_value.get()}')
                self.txtarea.insert(END,f"\nThe sum of the ycos(x):----->{y_cos_x_sum}")
                self.txtarea.insert(END,f"\nThe sum of the ysin(x):----->{y_sin_x_sum}")
                self.txtarea.insert(END,'\n*************************************************************************************************')
            
                self.txtarea.insert(END,'\n*************************************************************************************************\n')
                a=float(float(2/self.x_value.get()) *float(self.final_value.get()))
                a0=a/2
                a1=float(float(2/self.x_value.get()) *float(y_cos_x_sum))
                b1=float(float(2/self.x_value.get()) *float(y_sin_x_sum))
                self.txtarea.insert(END,f'\na0 is:------->{a0}')
                self.txtarea.insert(END,f"\na1 is:------->{a1}")
                self.txtarea.insert(END,f"\nb1 is:------->{b1}")
                self.txtarea.insert(END,'\n*************************************************************************************************')
            if(self.x_value.get()==10):
                x_value_num=[]
                y_value_num=[]
                y_sin_x_num=[]
                y_cos_x_num=[]

                self.final_value.set(float(
                            (float(self.y_value1.get()))+
                            (float(self.y_value2.get()))+
                            (float(self.y_value3.get()))+
                            (float(self.y_value4.get()))+
                            (float(self.y_value5.get()))+
                            (float(self.y_value6.get()))+
                            (float(self.y_value7.get()))+
                            (float(self.y_value8.get()))+
                            (float(self.y_value9.get()))+
                            (float(self.y_value10.get()))
                             )
                            )  
                self.txtarea.delete('1.0',END)
                self.txtarea.insert(END,'\t\t\t\t\tPractical Hormonic Analysis')
                self.txtarea.insert(END,f"\nNumber of X value is:------->{self.x_value.get()}")
                self.txtarea.insert(END,f"\nNumber of Y value:---------->{self.y_value.get()}")
                self.txtarea.insert(END,f"\nNumber of Hormonic value:--->{self.hormonics.get()}")
                self.txtarea.insert(END,'\n\n*************************************************************************************************')
                self.txtarea.insert(END,"\nsin(x)\t\tcos(x)\t\tysin(x)\t\tycos(x)")
                self.txtarea.insert(END,'\n*************************************************************************************************')
        
                sin_x_1=round(float(math.sin((self.x_value1.get()*3.14)/180)),3)
                x_value_num.append(sin_x_1)
                sin_x_2=round(float(math.sin((self.x_value2.get()*3.14)/180)),3)
                x_value_num.append(sin_x_2)
                sin_x_3=round(float(math.sin((self.x_value3.get()*3.14)/180)),3)
                x_value_num.append(sin_x_3)
                sin_x_4=round(float(math.sin((self.x_value4.get()*3.14)/180)),3)
                x_value_num.append(sin_x_4)
                sin_x_5=round(float(math.sin((self.x_value5.get()*3.14)/180)),3)
                x_value_num.append(sin_x_5)
                sin_x_6=round(float(math.sin((self.x_value6.get()*3.14)/180)),3)
                x_value_num.append(sin_x_6)
                sin_x_7=round(float(math.sin((self.x_value7.get()*3.14)/180)),3)
                x_value_num.append(sin_x_7)
                sin_x_8=round(float(math.sin((self.x_value8.get()*3.14)/180)),3)
                x_value_num.append(sin_x_8)
                sin_x_9=round(float(math.sin((self.x_value9.get()*3.14)/180)),3)
                x_value_num.append(sin_x_9)
                sin_x_10=round(float(math.sin((self.x_value10.get()*3.14)/180)),3)
                x_value_num.append(sin_x_10)
        
                cos_x_1=round(float(math.cos((self.x_value1.get()*3.14)/180)),3)
                y_value_num.append(cos_x_1)
                cos_x_2=round(float(math.cos((self.x_value2.get()*3.14)/180)),3)
                y_value_num.append(cos_x_2)
                cos_x_3=round(float(math.cos((self.x_value3.get()*3.14)/180)),3)
                y_value_num.append(cos_x_3)
                cos_x_4=round(float(math.cos((self.x_value4.get()*3.14)/180)),3)
                y_value_num.append(cos_x_4)
                cos_x_5=round(float(math.cos((self.x_value5.get()*3.14)/180)),3)
                y_value_num.append(cos_x_5)
                cos_x_6=round(float(math.cos((self.x_value6.get()*3.14)/180)),3)
                y_value_num.append(cos_x_6)
                cos_x_7=round(float(math.cos((self.x_value7.get()*3.14)/180)),3)
                y_value_num.append(cos_x_7)
                cos_x_8=round(float(math.cos((self.x_value8.get()*3.14)/180)),3)
                y_value_num.append(cos_x_8)
                cos_x_9=round(float(math.cos((self.x_value9.get()*3.14)/180)),3)
                y_value_num.append(cos_x_9)
                cos_x_10=round(float(math.cos((self.x_value10.get()*3.14)/180)),3)
                y_value_num.append(cos_x_10)

                y_sin_x_1=round(float(float(self.y_value1.get()) * sin_x_1),3)
                y_sin_x_num.append(y_sin_x_1)
                y_sin_x_2=round(float(float(self.y_value2.get()) * sin_x_2),3)
                y_sin_x_num.append(y_sin_x_2)
                y_sin_x_3=round(float(float(self.y_value3.get()) * sin_x_3),3)
                y_sin_x_num.append(y_sin_x_3)
                y_sin_x_4=round(float(float(self.y_value4.get()) * sin_x_4),3)
                y_sin_x_num.append(y_sin_x_4)
                y_sin_x_5=round(float(float(self.y_value5.get()) * sin_x_5),3)
                y_sin_x_num.append(y_sin_x_5)
                y_sin_x_6=round(float(float(self.y_value6.get()) * sin_x_6),3)
                y_sin_x_num.append(y_sin_x_6)
                y_sin_x_7=round(float(float(self.y_value7.get()) * sin_x_7),3)
                y_sin_x_num.append(y_sin_x_7)
                y_sin_x_8=round(float(float(self.y_value8.get()) * sin_x_8),3)
                y_sin_x_num.append(y_sin_x_8)
                y_sin_x_9=round(float(float(self.y_value9.get()) * sin_x_9),3)
                y_sin_x_num.append(y_sin_x_9)
                y_sin_x_10=round(float(float(self.y_value10.get()) * sin_x_10),3)
                y_sin_x_num.append(y_sin_x_10)
        
                y_cos_x_1=round(float(float(self.y_value1.get()) * cos_x_1),3)
                y_cos_x_num.append(y_cos_x_1)
                y_cos_x_2=round(float(float(self.y_value2.get()) * cos_x_2),3)
                y_cos_x_num.append(y_cos_x_2)
                y_cos_x_3=round(float(float(self.y_value3.get()) * cos_x_3),3)
                y_cos_x_num.append(y_cos_x_3)
                y_cos_x_4=round(float(float(self.y_value4.get()) * cos_x_4),3)
                y_cos_x_num.append(y_cos_x_4)
                y_cos_x_5=round(float(float(self.y_value5.get()) * cos_x_5),3)
                y_cos_x_num.append(y_cos_x_5)
                y_cos_x_6=round(float(float(self.y_value6.get()) * cos_x_6),3)
                y_cos_x_num.append(y_cos_x_6)
                y_cos_x_7=round(float(float(self.y_value7.get()) * cos_x_7),3)
                y_cos_x_num.append(y_cos_x_7)
                y_cos_x_8=round(float(float(self.y_value8.get()) * cos_x_8),3)
                y_cos_x_num.append(y_cos_x_8)
                y_cos_x_9=round(float(float(self.y_value9.get()) * cos_x_9),3)
                y_cos_x_num.append(y_cos_x_9)
                y_cos_x_10=round(float(float(self.y_value10.get()) * cos_x_10),3)
                y_cos_x_num.append(y_cos_x_10)
        
        
                y_cos_x_sum=y_cos_x_1 + y_cos_x_2 + y_cos_x_3 + y_cos_x_4 + y_cos_x_5 + y_cos_x_6+ y_cos_x_7+ y_cos_x_8+ y_cos_x_9+ y_cos_x_10
                y_sin_x_sum=y_sin_x_1 + y_sin_x_2 + y_sin_x_3 + y_sin_x_4 + y_sin_x_5 + y_sin_x_6+ y_sin_x_7+ y_sin_x_8+ y_sin_x_9+ y_sin_x_10
           
                           
                for i in range(10):
                    self.txtarea.insert(END,f'\n{x_value_num[i]}\t\t{y_value_num[i]}\t\t{y_sin_x_num[i]}\t\t{y_cos_x_num[i]}')

                self.txtarea.insert(END,'\n*************************************************************************************************\n')
                self.txtarea.insert(END,f'\nThe sum of the y is -------->{self.final_value.get()}')
                self.txtarea.insert(END,f"\nThe sum of the ycos(x):----->{y_cos_x_sum}")
                self.txtarea.insert(END,f"\nThe sum of the ysin(x):----->{y_sin_x_sum}")
                self.txtarea.insert(END,'\n*************************************************************************************************')
            
                self.txtarea.insert(END,'\n*************************************************************************************************\n')
                a=float(float(2/self.x_value.get()) *float(self.final_value.get()))
                a0=a/2
                a1=float(float(2/self.x_value.get()) *float(y_cos_x_sum))
                b1=float(float(2/self.x_value.get()) *float(y_sin_x_sum))
                self.txtarea.insert(END,f'\na0 is:------->{a0}')
                self.txtarea.insert(END,f"\na1 is:------->{a1}")
                self.txtarea.insert(END,f"\nb1 is:------->{b1}")
                self.txtarea.insert(END,'\n*************************************************************************************************')
            if(self.x_value.get()==11):
                x_value_num=[]
                y_value_num=[]
                y_sin_x_num=[]
                y_cos_x_num=[]

                self.final_value.set(float(
                            (float(self.y_value1.get()))+
                            (float(self.y_value2.get()))+
                            (float(self.y_value3.get()))+
                            (float(self.y_value4.get()))+
                            (float(self.y_value5.get()))+
                            (float(self.y_value6.get()))+
                            (float(self.y_value7.get()))+
                            (float(self.y_value8.get()))+
                            (float(self.y_value9.get()))+
                            (float(self.y_value10.get()))+
                            (float(self.y_value11.get()))
                             )
                            )  
                self.txtarea.delete('1.0',END)
                self.txtarea.insert(END,'\t\t\t\t\tPractical Hormonic Analysis')
                self.txtarea.insert(END,f"\nNumber of X value is:------->{self.x_value.get()}")
                self.txtarea.insert(END,f"\nNumber of Y value:---------->{self.y_value.get()}")
                self.txtarea.insert(END,f"\nNumber of Hormonic value:--->{self.hormonics.get()}")
                self.txtarea.insert(END,'\n\n*************************************************************************************************')
                self.txtarea.insert(END,"\nsin(x)\t\tcos(x)\t\tysin(x)\t\tycos(x)")
                self.txtarea.insert(END,'\n*************************************************************************************************')
        
                sin_x_1=round(float(math.sin((self.x_value1.get()*3.14)/180)),3)
                x_value_num.append(sin_x_1)
                sin_x_2=round(float(math.sin((self.x_value2.get()*3.14)/180)),3)
                x_value_num.append(sin_x_2)
                sin_x_3=round(float(math.sin((self.x_value3.get()*3.14)/180)),3)
                x_value_num.append(sin_x_3)
                sin_x_4=round(float(math.sin((self.x_value4.get()*3.14)/180)),3)
                x_value_num.append(sin_x_4)
                sin_x_5=round(float(math.sin((self.x_value5.get()*3.14)/180)),3)
                x_value_num.append(sin_x_5)
                sin_x_6=round(float(math.sin((self.x_value6.get()*3.14)/180)),3)
                x_value_num.append(sin_x_6)
                sin_x_7=round(float(math.sin((self.x_value7.get()*3.14)/180)),3)
                x_value_num.append(sin_x_7)
                sin_x_8=round(float(math.sin((self.x_value8.get()*3.14)/180)),3)
                x_value_num.append(sin_x_8)
                sin_x_9=round(float(math.sin((self.x_value9.get()*3.14)/180)),3)
                x_value_num.append(sin_x_9)
                sin_x_10=round(float(math.sin((self.x_value10.get()*3.14)/180)),3)
                x_value_num.append(sin_x_10)
                sin_x_11=round(float(math.sin((self.x_value11.get()*3.14)/180)),3)
                x_value_num.append(sin_x_11)
        
                cos_x_1=round(float(math.cos((self.x_value1.get()*3.14)/180)),3)
                y_value_num.append(cos_x_1)
                cos_x_2=round(float(math.cos((self.x_value2.get()*3.14)/180)),3)
                y_value_num.append(cos_x_2)
                cos_x_3=round(float(math.cos((self.x_value3.get()*3.14)/180)),3)
                y_value_num.append(cos_x_3)
                cos_x_4=round(float(math.cos((self.x_value4.get()*3.14)/180)),3)
                y_value_num.append(cos_x_4)
                cos_x_5=round(float(math.cos((self.x_value5.get()*3.14)/180)),3)
                y_value_num.append(cos_x_5)
                cos_x_6=round(float(math.cos((self.x_value6.get()*3.14)/180)),3)
                y_value_num.append(cos_x_6)
                cos_x_7=round(float(math.cos((self.x_value7.get()*3.14)/180)),3)
                y_value_num.append(cos_x_7)
                cos_x_8=round(float(math.cos((self.x_value8.get()*3.14)/180)),3)
                y_value_num.append(cos_x_8)
                cos_x_9=round(float(math.cos((self.x_value9.get()*3.14)/180)),3)
                y_value_num.append(cos_x_9)
                cos_x_10=round(float(math.cos((self.x_value10.get()*3.14)/180)),3)
                y_value_num.append(cos_x_10)
                cos_x_11=round(float(math.cos((self.x_value11.get()*3.14)/180)),3)
                y_value_num.append(cos_x_11)

                y_sin_x_1=round(float(float(self.y_value1.get()) * sin_x_1),3)
                y_sin_x_num.append(y_sin_x_1)
                y_sin_x_2=round(float(float(self.y_value2.get()) * sin_x_2),3)
                y_sin_x_num.append(y_sin_x_2)
                y_sin_x_3=round(float(float(self.y_value3.get()) * sin_x_3),3)
                y_sin_x_num.append(y_sin_x_3)
                y_sin_x_4=round(float(float(self.y_value4.get()) * sin_x_4),3)
                y_sin_x_num.append(y_sin_x_4)
                y_sin_x_5=round(float(float(self.y_value5.get()) * sin_x_5),3)
                y_sin_x_num.append(y_sin_x_5)
                y_sin_x_6=round(float(float(self.y_value6.get()) * sin_x_6),3)
                y_sin_x_num.append(y_sin_x_6)
                y_sin_x_7=round(float(float(self.y_value7.get()) * sin_x_7),3)
                y_sin_x_num.append(y_sin_x_7)
                y_sin_x_8=round(float(float(self.y_value8.get()) * sin_x_8),3)
                y_sin_x_num.append(y_sin_x_8)
                y_sin_x_9=round(float(float(self.y_value9.get()) * sin_x_9),3)
                y_sin_x_num.append(y_sin_x_9)
                y_sin_x_10=round(float(float(self.y_value10.get()) * sin_x_10),3)
                y_sin_x_num.append(y_sin_x_10)
                y_sin_x_11=round(float(float(self.y_value11.get()) * sin_x_11),3)
                y_sin_x_num.append(y_sin_x_11)
        
                y_cos_x_1=round(float(float(self.y_value1.get()) * cos_x_1),3)
                y_cos_x_num.append(y_cos_x_1)
                y_cos_x_2=round(float(float(self.y_value2.get()) * cos_x_2),3)
                y_cos_x_num.append(y_cos_x_2)
                y_cos_x_3=round(float(float(self.y_value3.get()) * cos_x_3),3)
                y_cos_x_num.append(y_cos_x_3)
                y_cos_x_4=round(float(float(self.y_value4.get()) * cos_x_4),3)
                y_cos_x_num.append(y_cos_x_4)
                y_cos_x_5=round(float(float(self.y_value5.get()) * cos_x_5),3)
                y_cos_x_num.append(y_cos_x_5)
                y_cos_x_6=round(float(float(self.y_value6.get()) * cos_x_6),3)
                y_cos_x_num.append(y_cos_x_6)
                y_cos_x_7=round(float(float(self.y_value7.get()) * cos_x_7),3)
                y_cos_x_num.append(y_cos_x_7)
                y_cos_x_8=round(float(float(self.y_value8.get()) * cos_x_8),3)
                y_cos_x_num.append(y_cos_x_8)
                y_cos_x_9=round(float(float(self.y_value9.get()) * cos_x_9),3)
                y_cos_x_num.append(y_cos_x_9)
                y_cos_x_10=round(float(float(self.y_value10.get()) * cos_x_10),3)
                y_cos_x_num.append(y_cos_x_10)
                y_cos_x_11=round(float(float(self.y_value11.get()) * cos_x_11),3)
                y_cos_x_num.append(y_cos_x_11)
        
        
                y_cos_x_sum=y_cos_x_1 + y_cos_x_2 + y_cos_x_3 + y_cos_x_4 + y_cos_x_5 + y_cos_x_6+ y_cos_x_7+ y_cos_x_8+ y_cos_x_9+ y_cos_x_10+ y_cos_x_11
                y_sin_x_sum=y_sin_x_1 + y_sin_x_2 + y_sin_x_3 + y_sin_x_4 + y_sin_x_5 + y_sin_x_6+ y_sin_x_7+ y_sin_x_8+ y_sin_x_9+ y_sin_x_10+ y_sin_x_11
           
                           
                for i in range(11):
                    self.txtarea.insert(END,f'\n{x_value_num[i]}\t\t{y_value_num[i]}\t\t{y_sin_x_num[i]}\t\t{y_cos_x_num[i]}')

                self.txtarea.insert(END,'\n*************************************************************************************************\n')
                self.txtarea.insert(END,f'\nThe sum of the y is -------->{self.final_value.get()}')
                self.txtarea.insert(END,f"\nThe sum of the ycos(x):----->{y_cos_x_sum}")
                self.txtarea.insert(END,f"\nThe sum of the ysin(x):----->{y_sin_x_sum}")
                self.txtarea.insert(END,'\n*************************************************************************************************')
            
                self.txtarea.insert(END,'\n*************************************************************************************************\n')
                a=float(float(2/self.x_value.get()) *float(self.final_value.get()))
                a0=a/2
                a1=float(float(2/self.x_value.get()) *float(y_cos_x_sum))
                b1=float(float(2/self.x_value.get()) *float(y_sin_x_sum))
                self.txtarea.insert(END,f'\na0 is:------->{a0}')
                self.txtarea.insert(END,f"\na1 is:------->{a1}")
                self.txtarea.insert(END,f"\nb1 is:------->{b1}")
                self.txtarea.insert(END,'\n*************************************************************************************************')
            if(self.x_value.get()==12):
                x_value_num=[]
                y_value_num=[]
                y_sin_x_num=[]
                y_cos_x_num=[]

                self.final_value.set(float(
                            (float(self.y_value1.get()))+
                            (float(self.y_value2.get()))+
                            (float(self.y_value3.get()))+
                            (float(self.y_value4.get()))+
                            (float(self.y_value5.get()))+
                            (float(self.y_value6.get()))+
                            (float(self.y_value7.get()))+
                            (float(self.y_value8.get()))+
                            (float(self.y_value9.get()))+
                            (float(self.y_value10.get()))+
                            (float(self.y_value11.get()))
                            (float(self.y_value12.get()))
                             )
                            )  
                self.txtarea.delete('1.0',END)
                self.txtarea.insert(END,'\t\t\t\t\tPractical Hormonic Analysis')
                self.txtarea.insert(END,f"\nNumber of X value is:------->{self.x_value.get()}")
                self.txtarea.insert(END,f"\nNumber of Y value:---------->{self.y_value.get()}")
                self.txtarea.insert(END,f"\nNumber of Hormonic value:--->{self.hormonics.get()}")
                self.txtarea.insert(END,'\n\n*************************************************************************************************')
                self.txtarea.insert(END,"\nsin(x)\t\tcos(x)\t\tysin(x)\t\tycos(x)")
                self.txtarea.insert(END,'\n*************************************************************************************************')
        
                sin_x_1=round(float(math.sin((self.x_value1.get()*3.14)/180)),3)
                x_value_num.append(sin_x_1)
                sin_x_2=round(float(math.sin((self.x_value2.get()*3.14)/180)),3)
                x_value_num.append(sin_x_2)
                sin_x_3=round(float(math.sin((self.x_value3.get()*3.14)/180)),3)
                x_value_num.append(sin_x_3)
                sin_x_4=round(float(math.sin((self.x_value4.get()*3.14)/180)),3)
                x_value_num.append(sin_x_4)
                sin_x_5=round(float(math.sin((self.x_value5.get()*3.14)/180)),3)
                x_value_num.append(sin_x_5)
                sin_x_6=round(float(math.sin((self.x_value6.get()*3.14)/180)),3)
                x_value_num.append(sin_x_6)
                sin_x_7=round(float(math.sin((self.x_value7.get()*3.14)/180)),3)
                x_value_num.append(sin_x_7)
                sin_x_8=round(float(math.sin((self.x_value8.get()*3.14)/180)),3)
                x_value_num.append(sin_x_8)
                sin_x_9=round(float(math.sin((self.x_value9.get()*3.14)/180)),3)
                x_value_num.append(sin_x_9)
                sin_x_10=round(float(math.sin((self.x_value10.get()*3.14)/180)),3)
                x_value_num.append(sin_x_10)
                sin_x_11=round(float(math.sin((self.x_value11.get()*3.14)/180)),3)
                x_value_num.append(sin_x_11)
                sin_x_12=round(float(math.sin((self.x_value12.get()*3.14)/180)),3)
                x_value_num.append(sin_x_12)
        
                cos_x_1=round(float(math.cos((self.x_value1.get()*3.14)/180)),3)
                y_value_num.append(cos_x_1)
                cos_x_2=round(float(math.cos((self.x_value2.get()*3.14)/180)),3)
                y_value_num.append(cos_x_2)
                cos_x_3=round(float(math.cos((self.x_value3.get()*3.14)/180)),3)
                y_value_num.append(cos_x_3)
                cos_x_4=round(float(math.cos((self.x_value4.get()*3.14)/180)),3)
                y_value_num.append(cos_x_4)
                cos_x_5=round(float(math.cos((self.x_value5.get()*3.14)/180)),3)
                y_value_num.append(cos_x_5)
                cos_x_6=round(float(math.cos((self.x_value6.get()*3.14)/180)),3)
                y_value_num.append(cos_x_6)
                cos_x_7=round(float(math.cos((self.x_value7.get()*3.14)/180)),3)
                y_value_num.append(cos_x_7)
                cos_x_8=round(float(math.cos((self.x_value8.get()*3.14)/180)),3)
                y_value_num.append(cos_x_8)
                cos_x_9=round(float(math.cos((self.x_value9.get()*3.14)/180)),3)
                y_value_num.append(cos_x_9)
                cos_x_10=round(float(math.cos((self.x_value10.get()*3.14)/180)),3)
                y_value_num.append(cos_x_10)
                cos_x_11=round(float(math.cos((self.x_value11.get()*3.14)/180)),3)
                y_value_num.append(cos_x_11)
                cos_x_12=round(float(math.cos((self.x_value12.get()*3.14)/180)),3)
                y_value_num.append(cos_x_12)

                y_sin_x_1=round(float(float(self.y_value1.get()) * sin_x_1),3)
                y_sin_x_num.append(y_sin_x_1)
                y_sin_x_2=round(float(float(self.y_value2.get()) * sin_x_2),3)
                y_sin_x_num.append(y_sin_x_2)
                y_sin_x_3=round(float(float(self.y_value3.get()) * sin_x_3),3)
                y_sin_x_num.append(y_sin_x_3)
                y_sin_x_4=round(float(float(self.y_value4.get()) * sin_x_4),3)
                y_sin_x_num.append(y_sin_x_4)
                y_sin_x_5=round(float(float(self.y_value5.get()) * sin_x_5),3)
                y_sin_x_num.append(y_sin_x_5)
                y_sin_x_6=round(float(float(self.y_value6.get()) * sin_x_6),3)
                y_sin_x_num.append(y_sin_x_6)
                y_sin_x_7=round(float(float(self.y_value7.get()) * sin_x_7),3)
                y_sin_x_num.append(y_sin_x_7)
                y_sin_x_8=round(float(float(self.y_value8.get()) * sin_x_8),3)
                y_sin_x_num.append(y_sin_x_8)
                y_sin_x_9=round(float(float(self.y_value9.get()) * sin_x_9),3)
                y_sin_x_num.append(y_sin_x_9)
                y_sin_x_10=round(float(float(self.y_value10.get()) * sin_x_10),3)
                y_sin_x_num.append(y_sin_x_10)
                y_sin_x_11=round(float(float(self.y_value11.get()) * sin_x_11),3)
                y_sin_x_num.append(y_sin_x_11)
                y_sin_x_12=round(float(float(self.y_value12.get()) * sin_x_12),3)
                y_sin_x_num.append(y_sin_x_12)
        
                y_cos_x_1=round(float(float(self.y_value1.get()) * cos_x_1),3)
                y_cos_x_num.append(y_cos_x_1)
                y_cos_x_2=round(float(float(self.y_value2.get()) * cos_x_2),3)
                y_cos_x_num.append(y_cos_x_2)
                y_cos_x_3=round(float(float(self.y_value3.get()) * cos_x_3),3)
                y_cos_x_num.append(y_cos_x_3)
                y_cos_x_4=round(float(float(self.y_value4.get()) * cos_x_4),3)
                y_cos_x_num.append(y_cos_x_4)
                y_cos_x_5=round(float(float(self.y_value5.get()) * cos_x_5),3)
                y_cos_x_num.append(y_cos_x_5)
                y_cos_x_6=round(float(float(self.y_value6.get()) * cos_x_6),3)
                y_cos_x_num.append(y_cos_x_6)
                y_cos_x_7=round(float(float(self.y_value7.get()) * cos_x_7),3)
                y_cos_x_num.append(y_cos_x_7)
                y_cos_x_8=round(float(float(self.y_value8.get()) * cos_x_8),3)
                y_cos_x_num.append(y_cos_x_8)
                y_cos_x_9=round(float(float(self.y_value9.get()) * cos_x_9),3)
                y_cos_x_num.append(y_cos_x_9)
                y_cos_x_10=round(float(float(self.y_value10.get()) * cos_x_10),3)
                y_cos_x_num.append(y_cos_x_10)
                y_cos_x_11=round(float(float(self.y_value11.get()) * cos_x_11),3)
                y_cos_x_num.append(y_cos_x_11)
                y_cos_x_12=round(float(float(self.y_value12.get()) * cos_x_12),3)
                y_cos_x_num.append(y_cos_x_12)
        
        
                y_cos_x_sum=y_cos_x_1 + y_cos_x_2 + y_cos_x_3 + y_cos_x_4 + y_cos_x_5 + y_cos_x_6+ y_cos_x_7+ y_cos_x_8+ y_cos_x_9+ y_cos_x_10+ y_cos_x_11+ y_cos_x_12
                y_sin_x_sum=y_sin_x_1 + y_sin_x_2 + y_sin_x_3 + y_sin_x_4 + y_sin_x_5 + y_sin_x_6+ y_sin_x_7+ y_sin_x_8+ y_sin_x_9+ y_sin_x_10+ y_sin_x_11+ y_sin_x_12
           
                           
                for i in range(12):
                    self.txtarea.insert(END,f'\n{x_value_num[i]}\t\t{y_value_num[i]}\t\t{y_sin_x_num[i]}\t\t{y_cos_x_num[i]}')

                self.txtarea.insert(END,'\n*************************************************************************************************\n')
                self.txtarea.insert(END,f'\nThe sum of the y is -------->{self.final_value.get()}')
                self.txtarea.insert(END,f"\nThe sum of the ycos(x):----->{y_cos_x_sum}")
                self.txtarea.insert(END,f"\nThe sum of the ysin(x):----->{y_sin_x_sum}")
                self.txtarea.insert(END,'\n*************************************************************************************************')
            
                self.txtarea.insert(END,'\n*************************************************************************************************\n')
                a=float(float(2/self.x_value.get()) *float(self.final_value.get()))
                a0=a/2
                a1=float(float(2/self.x_value.get()) *float(y_cos_x_sum))
                b1=float(float(2/self.x_value.get()) *float(y_sin_x_sum))
                self.txtarea.insert(END,f'\na0 is:------->{a0}')
                self.txtarea.insert(END,f"\na1 is:------->{a1}")
                self.txtarea.insert(END,f"\nb1 is:------->{b1}")
                self.txtarea.insert(END,'\n*************************************************************************************************')
            
    def save_bill(self):
        for i in range(1):
            number=random.randint(1,6)
        op=messagebox.askyesno("Save the problum","Do you want to save the bill")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open('bills/'+str(number)+".txt",'w')
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Problumn number:{number} saved successfully")
        else:
            return
                    
                
root=Tk()
obj=practical_harmonic_anysis(root)
root.mainloop()
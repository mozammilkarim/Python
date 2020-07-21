from tkinter import *
class billWindow:
    def __init__(self,root):
        self.root=root
        self.root.title('Welcome to My Billing')
        self.root.geometry('1200x700')
        self.root.minsize(1200,500)
        #title heading
        titleLabel=Label(self.root,bg='grey',bd=8,relief=RIDGE,font='lucida 20',text='Welcome to SMK Billing Software')
        titleLabel.pack(fill=X)
        #customer details
        cFrame=LabelFrame(self.root,text="Customer Details",fg='red',font='lucida 20',bd=8,relief=RIDGE)
        #relWidth sets the width  relative to its parent and  x , y are coordinates
        cFrame.place(x=0,y=50,relwidth=1)
        global j
        j=0
        self.cDetailsList=['Customer Name','Contact No.','Bill No.']
        self.cDetailsLabel=[]
        self.cDetailsStr=[StringVar(),StringVar(),StringVar()]
        self.cDetailsEntry=[]
        for i in self.cDetailsStr:
            self.cDetailsLabel.append(Label(cFrame,text=self.cDetailsList[j],fg='red',font='lucida 15').grid(row=0,column=j*2))
            self.cDetailsEntry.append(Entry(cFrame,text=self.cDetailsStr[j],font='lucida 15',width=20).grid(row=0,column=j*2+1,padx=2,pady=2))
            self.cDetailsStr[j].set('')
            j+=1
        
        #search customer
        self.cSearchBtn=Button(cFrame,text='Search',width=10).grid(row=0,column=6,pady=5)
        #grocery section
        
        gFrame=LabelFrame(self.root,text="Grocery",fg='red',font='lucida 20',bd=8,relief=RIDGE)
        gFrame.place(x=0,y=150,relwidth=0.30)

        j=0
        self.gDetailsList=['Rice(kg)','Wheat Flour(kg)','Oil(l)','Red Pulse(kg)','Sugar(kg)']
        self.gDetailsLabel=[]
        self.gDetailsStr=[StringVar(),StringVar(),StringVar(),StringVar(),StringVar()]
        self.gDetailsEntry=[]
        self.gRateList=[40,100,80,41,39]
        for i in self.gDetailsStr:
            self.gDetailsLabel.append(Label(gFrame,text=self.gDetailsList[j],fg='red',font='lucida 15').grid(row=j,column=0))
            self.gDetailsEntry.append(Entry(gFrame,text=self.gDetailsStr[j],font='lucida 15',width=18).grid(row=j,column=1,padx=2,pady=2))
            self.gDetailsStr[j].set('')
            j+=1
        
        #cold drink section
        drinkFrame=LabelFrame(self.root,text='Cold Drinks',font='lucida 20',fg='red',relief=GROOVE,bd=8)
        drinkFrame.place(x=400,y=150,relwidth=0.30)
        self.drinkList=['maaza','slice','Thumbs Up','Coca Cola']
        self.drinkEntryValue=[StringVar(),StringVar(),StringVar(),StringVar()]
        self.drinkLabelList=[]
        self.drinkEntryList=[]
        self.drinkRateList=[80,75,80,90]
        j=0
        for i in self.drinkList:
            self.drinkLabelList.append(Label(drinkFrame,text=self.drinkList[j],font='lucida 15',fg='red').grid(row=j,column=0,padx=2,pady=2))
            self.drinkEntryList.append(Entry(drinkFrame,text=self.drinkEntryValue[j]).grid(row=j,column=1,padx=2,pady=2))
            self.drinkEntryValue[j].set('')
            j+=1
        # bill area
        billAreaF=Frame(self.root,relief=GROOVE,bd=8)
        billAreaF.place(x=800,y=150,relwidth=0.35,height=600)
        # billAreaF.pack()
        #scroll Bar fro bill Area
        
        billtitle=Label(billAreaF,text='Bill Area',font='lucida 20',fg='green',bd=8,relief=RIDGE)
        billtitle.pack(fill=X)
        
        self.billAreaContent=Label(billAreaF,text='Welcome!!',font='lucida 15',bd=8)
        self.billAreaContent.pack(fill=X)
        #scroll bars cannot work with
        
        #now buttons
        btnFrame=LabelFrame(self.root,relief=SUNKEN,text='Billing Menu',bd=8,font='lucida 28')
        btnFrame.place(x=0,y=350,relwidth=.50)
        clearBtn=Button(btnFrame,text='Clear',font='lucida 18',relief=SUNKEN,bd=8,fg='blue',command=self.clearFunc).pack(side=LEFT,padx=10)
        generateBtn=Button(btnFrame,text='Generate Bill',font='lucida 18',relief=SUNKEN,bd=8,fg='blue',command=self.generateBillFunc).pack(side=LEFT,padx=10)
        exitBtn=Button(btnFrame,text='Exit',font='lucida 18',relief=SUNKEN,bd=8,fg='blue',command=self.exitFunc).pack(side=LEFT,padx=10)
        
    def exitFunc(self):
        exit()
    def clearFunc(self):
        for i in self.gDetailsStr:
            i.set('')
        for i in self.drinkEntryValue:
            i.set('')
        for i in self.cDetailsStr:
            i.set('')
        self.billAreaContent.config(text='Welcome!!')
    def generateBillFunc(self):
        billContent='Welcome to SYED Retails\n'
        # print(self.cDetailsStr[2].get())
        if self.cDetailsStr[2].get()=='' or self.cDetailsStr[1].get()=='' or self.cDetailsStr[0].get()=='' or self.cDetailsStr[1].get().isdigit()!=TRUE:
            self.billAreaContent.config(text='First Enter Details Properly')
            return
        billContent+=f'Phone No. 7827141330\nBill No. {self.cDetailsStr[2].get()} \n'
        billContent+=f'Contact No. {self.cDetailsStr[1].get()} \n'
        billContent+=f'Customer Name {self.cDetailsStr[0].get()} \n'
        global total
        total=0
        global j
        j=0
        for i in self.gDetailsStr:
            if i.get()!='' and i.get().isdigit() :
                billContent+=f'{self.gDetailsList[j]}-- {i.get()}\n'
                total+=float(int(i.get())*self.gRateList[j])
            j+=1
        j=0
        for i in self.drinkEntryValue:
            if i.get()!='' and i.get().isdigit():
                billContent+=f'{self.drinkList[j]}-- {i.get()}\n'
                total+=float(int(i.get())*self.drinkRateList[j])
            j+=1
        
        billContent+=f'Total={total}'
        self.billAreaContent.config(text=billContent)

root=Tk()
mybill=billWindow(root)
root.mainloop()
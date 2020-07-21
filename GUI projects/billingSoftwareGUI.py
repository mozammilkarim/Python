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

        cname=Label(cFrame,text='Customer Name',fg='red',font='lucida 15',bd=8,relief=RIDGE)
        cname.grid()
        cNameValueStr=StringVar()
        cNameValue=Entry(cFrame,text=cNameValueStr,width=20)
        cNameValue.grid(row=0,column=1,padx=10,pady=5)

        cPhone=Label(cFrame,text='Customer Name',fg='red',font='lucida 15',bd=8,relief=RIDGE)
        cPhone.grid(row=0,column=2)
        cPhoneValueStr=StringVar()
        cPhoneValue=Entry(cFrame,text=cPhoneValueStr,width=20)
        cPhoneValue.grid(row=0,column=3,padx=10,pady=5)

        cBillNo=Label(cFrame,text='Customer Name',fg='red',font='lucida 15',bd=8,relief=RIDGE)
        cBillNo.grid(row=0,column=4)
        cBillValueStr=StringVar()
        cBillValue=Entry(cFrame,text=cBillValueStr,width=20)
        cBillValue.grid(row=0,column=5,padx=10,pady=5)
        #search customer
        cSearchBtn=Button(cFrame,text='Search',width=10).grid(row=0,column=6,pady=5)
        #grocery section
        gFrame=LabelFrame(self.root,text="Grocery",fg='red',font='lucida 20',bd=8,relief=RIDGE)
        gFrame.place(x=0,y=130,relwidth=0.25)
        rice=Label(gFrame,text='Rice',fg='red',font='lucida 15')
        rice.grid(row=0,column=0,padx=2,pady=2)
        WheatFlour=Label(gFrame,text='WheatFlour',fg='red',font='lucida 15')
        WheatFlour.grid(row=1,column=0,padx=2,pady=2)
        Oil=Label(gFrame,text='Oil',fg='red',font='lucida 15')
        Oil.grid(row=2,column=0,padx=2,pady=2)
        Pulses=Label(gFrame,text='Pulses',fg='red',font='lucida 15')
        Pulses.grid(row=3,column=0,padx=2,pady=2)
        #grocery input Values
        groceryInputValue=["0","0","0","0"]
        global groceryEntryList
        groceryEntryList=[]
        global j
        j=0
        
        for i in groceryInputValue:
            groceryEntryList.append(Entry(gFrame,text=groceryInputValue[j]).grid(row=j,column=1,padx=2,pady=2))
            j+=1

        #cold drink section
        drinkFrame=LabelFrame(self.root,text='Cold Drinks',font='lucida 20',fg='red',relief=GROOVE,bd=8)
        drinkFrame.place(x=325,y=130,relwidth=0.25)
        drinkList=['maaza','slice','Thumbs Up','Coca Cola']
        drinkEntryValue=['','','','']
        global drinkLabelList
        drinkLabelList=[]
        global drinkEntryList
        drinkEntryList=[]
        j=0
        for i in drinkList:
            drinkLabelList.append(Label(drinkFrame,text=drinkList[j],font='lucida 15',fg='red').grid(row=j,column=0,padx=2,pady=2))
            drinkEntryList.append(Entry(drinkFrame,text=drinkEntryValue[j]).grid(row=j,column=1))
            j+=1
        # bill area
        billAreaF=LabelFrame(self.root,bg='grey',font='lucida 20',fg='red',relief=GROOVE,bd=8)
        billAreaF.place(x=640,y=150,relwidth=.50)
        # billAreaF.pack()
        billtitle=Label(billAreaF,text='Bill Area',font='lucida 20',fg='green',bd=8,relief=RIDGE)
        billtitle.pack(fill=X)
        billAreaContent=Label(billAreaF,text='Bill Area',font='lucida 15',bd=8)
        billAreaContent.pack(fill=X)
        #now buttons
        btnFrame=LabelFrame(self.root,relief=SUNKEN,text='Billing Menu',bd=8,font='lucida 28')
        btnFrame.place(x=0,y=300,relwidth=.50)
        totalBtn=Button(btnFrame,text='Total',font='lucida 18',relief=SUNKEN,bd=8,fg='blue',command=self.totalFunc).pack(side=LEFT,padx=10)
        clearBtn=Button(btnFrame,text='Clear',font='lucida 18',relief=SUNKEN,bd=8,fg='blue',command=self.clearFunc).pack(side=LEFT,padx=10)
        generateBtn=Button(btnFrame,text='Generate Bill',font='lucida 18',relief=SUNKEN,bd=8,fg='blue',command=self.generateBillFunc).pack(side=LEFT,padx=10)
        exitBtn=Button(btnFrame,text='Exit',font='lucida 18',relief=SUNKEN,bd=8,fg='blue',command=self.exitFunc).pack(side=LEFT,padx=10)
        
    def exitFunc(self):
        exit()
    def totalFunc(self):
        print('giving total')
        
        for i in drinkEntryList:
            pass
    def clearFunc(self):
        print('Clear total')
    def generateBillFunc(self):
        print('Clear total')

root=Tk()
mybill=billWindow(root)
root.mainloop()
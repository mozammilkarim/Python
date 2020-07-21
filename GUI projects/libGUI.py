from tkinter import *
root=Tk()
root.title('Syed Ji ki Library')
root.geometry('600x500')

global lbx # this is list box to display results
# library class to handle the functions of a library
class library:
    def __init__(self):
        self.libName="Syed\'S library"
        self.libList=[]
        #book list should be brought from a file
        #and added to libList
        try:
            #first create file if it does not exists
            file=open('GUI projects\libfile.txt','at')
            file.close()
            file=open('GUI projects\libfile.txt','rt')
            if file:
                # print(file.read())
                fileList=file.readlines()
                for item in fileList:
                    bookDetails=item.split(',')
                    borrwer=bookDetails[3].split()
                    self.libList.append([bookDetails[0],bookDetails[1],bookDetails[2],borrwer[0]])
            file.close()
        except :
            pass
        
        
    def printLibrary(self):
        global lbx
        #update the list
        lbx.delete(first=0,last='end')
        lbx.insert(0,'Books List from Our Lib')
        for x in self.libList:
            lbx.insert(END, f'{x[0]}')
        lbx.update()
    def addBook(self,bookname,author,usage):
        '''this function should not be available to users 
        , only for administrator'''
        # now add books from newList 
        # to your list and file
        for item in self.libList:
            if bookname==item[0]:
                #book exists
                print('Book exists in our library')
                return
        
        try:
            file=open('GUI projects\libfile.txt','at')
            file.writelines(f"{bookname},{author},{usage},no\n")
            self.libList.append([bookname,author,usage,'no'])
            file.close()
            lbx.delete(first=0,last='end')
            lbx.insert(END,"YOUR BOOK IS ADDED")
            lbx.update()
            
        except :
            pass
    def removeFromLib(self,bookname):
        '''this function should not be available to users 
        , only for administrator'''
        # 1 check if it is present
        global index 
        index=0 
        for item in self.libList:
            if bookname==item[0]:
                #book exists
                self.deleteBook(bookname,index)
                return
            index+=1
        #first delete from list and then add the new list to file
        print('Book Does not Exists in our library')
    def updateFile(self):
        try:
            file=open('GUI projects\libfile.txt','wt')
            file.truncate()
            file.close()
            file=open('GUI projects\libfile.txt','at')
            for item in self.libList:
                file.writelines(f"{item[0]},{item[1]},{item[2]},{item[3]}\n")
            file.close()
            
            
        except :
            pass
    def deleteBook(self,bookname,listIndex):
        print('Book is in our library\n Are sure to delete it?')
        choice=input()
        if choice=='no':
            return
        
        del self.libList[listIndex]
        print('deleted from list')
        self.updateFile()
    def borrowBook(self,bookname,borrower):
        # 1 check if it is present
        global index 
        index=0 
        for item in self.libList:
            if bookname==item[0]:
                break #book exists   
            index+=1
        #index =0 is for checking empty list
        if  index==len(self.libList):
            global lbx
            lbx.delete(first=0,last='end')
            lbx.insert(END,'Book Does not Exists in Our library')
            lbx.update()
            return
        if self.libList[index][3]!='no':
            #update the listbox
            
            lbx.delete(first=0,last='end')
            lbx.insert(END,f'{bookValue.get()} is borrowed by {mylib.libList[index][3]}')
            lbx.update()
            return
        
        self.libList[index][3]=borrower
        self.updateFile()
        lbx.delete(first=0,last='end')
        lbx.insert(END,f'{bookValue.get()} can be borrowed ')
        lbx.update()
        
    def returnBook(self,bookname):
        # 1 check if it is present
        index=0 
        for item in self.libList:
            if bookname==item[0] and self.libList[index][3]!='no':
                #book exists and is available from now
                self.libList[index][3]='no'
                self.updateFile()
                lbx.delete(first=0,last='end')
                lbx.insert(END,f'{bookValue.get()} is returned to library ')
                lbx.update()
                return
            index+=1
        
        
        lbx.delete(first=0,last='end')
        lbx.insert(END,"Either Book Does not Exists in Our library or is available")
        lbx.update()
        
    
#for GUI events
def addBookFunc(event):
    mylib.addBook(bookValue.get(),authorValue.get(),usageValue.get())
    
def borrowBookFunc(event):
    mylib.borrowBook(bookValue.get(),borrowerValue.get())
    
def returnBookFunc(event):
    mylib.returnBook(bookValue.get())
def viewBooksFunc(event):
    mylib.printLibrary()

#GUI work  
f=Frame(root)
f.pack(side=LEFT)
bookName=Label(f,text='Book Name',padx=8, pady=3, font="lucida 20 bold")
bookName.pack()
bookValue = StringVar()
bookValue.set("")
bookValue = Entry(f, textvar=bookValue, font="lucida")
bookValue.pack(anchor='n')

authorName=Label(f,text='AuthorName',padx=8, pady=3, font="lucida 18 bold")
authorName.pack()
authorValue = StringVar()
authorValue.set("")
authorValue = Entry(f, textvar=authorValue, font="lucida")
authorValue.pack()

usageName=Label(f,text='Usage Name',padx=8, pady=3, font="lucida 18 bold")
usageName.pack()
usageValue = StringVar()
usageValue.set("")
usageValue = Entry(f, textvar=usageValue, font="lucida")
usageValue.pack()

borrowerName=Label(f,text='Borrower Name',padx=8, pady=3, font="lucida 18 bold")
borrowerName.pack()
borrowerValue = StringVar()
borrowerValue.set("")
borrowerValue = Entry(f, textvar=borrowerValue, font="lucida")
borrowerValue.pack()

#now add buttons
addBook = Button(f, text="Add a Book", padx=8, pady=3, font="lucida")
addBook.pack(padx=10)
addBook.bind("<Button-1>", addBookFunc)
borrowBook = Button(f, text="Borrow a Book",padx=8, pady=3, font="lucida")
borrowBook.pack(padx=30)
borrowBook.bind("<Button-1>", borrowBookFunc)
returnBook = Button(f, text="return a Book", padx=8, pady=3,font="lucida")
returnBook.pack()
returnBook.bind("<Button-1>", returnBookFunc)
viewBooks = Button(f, text="View Books", padx=8, pady=3, font="lucida")
viewBooks.pack()
viewBooks.bind("<Button-1>", viewBooksFunc)
#adding list box to show all books in our library
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
# scrollbar.pack()
lbx = Listbox(root,yscrollcommand = scrollbar.set)
lbx.pack(padx=8,pady=20,side=RIGHT,fill=Y)
scrollbar.config(command=lbx.yview)
lbx.insert(0,'Use view Books Button')
mylib=library()
root.mainloop()

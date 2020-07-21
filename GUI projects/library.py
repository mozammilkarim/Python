"""This is my updated version of library with file Handling"""
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
        print('The books in',self.libName,'are')
        print('BookName','Author','Usage')
        for x in self.libList:
            print(f'{x[0]},\t{x[1]}\t,{x[2]}')
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
            print('Book Added')
            
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
        if index==0 or index==len(self.libList):
            print('Book Does not Exists in our library')
            return
        if self.libList[index][3]!='no':
            print(f'Book is already borrowed by {self.libList[index][3]} from  our library')
            return
        
        self.libList[index][3]=borrower
        self.updateFile()
    def returnBook(self,bookname):
        # 1 check if it is present
        global index 
        index=0 
        for item in self.libList:
            if bookname==item[0]and self.libList[index][3]!='no':
                #book exists and is available from now
                self.libList[index][3]='no'
                self.updateFile()
                return
            index+=1
        
        print('Book Does not Exists in our library')
        
# a specimen of a book
# name,author,usage,borrower for storage

myLib=library()
while 1:
    print('Enter Your Choice\n1)View books in library')
    print('2)Return book in library')
    print('3)Borrow a book from library\npress -1 for exit')
    choice=input()
    if choice=='1':
        myLib.printLibrary()
    elif choice=='2':
        #name,author,usage,borrower
        print('Enter The bookname')
        bookname=input()
        myLib.returnBook(bookname)
    elif choice=='3':
        print('Enter The bookname')
        bookname=input()
        print('Enter your name')
        borrower=input()
        myLib.borrowBook(bookname,borrower)
    elif choice=='-1':
        exit()
    else:
        print('wrong option choosed')



myBooks={
    'The Hounds of BaskerVilles':
    ['Conan Doyle','Good',''],
    'Think and become Rich':
    ['Unknown','High',''],
    'Rich Dad CashFlow Quadrant':
    ['Robert Kiyosaki','High','']
}

class library:
    def __init__(self,name,booksList):
        self.libName=name
        self.libList=booksList
    def printLibrary(self):
        print('The books in',self.libName,'are')
        for x in self.libList:
            print(x)
    def addBook(self,newList):
        # now add books from newList 
        # to your dictionary
        if bookname in self.libList:
            print('Book already present in Our Library')
            return
        for key in newList:
            self.libList[key]=newList[key]
    def removeFromLib(self,bookname):
        if (bookname in self.libList)==False:
            print('Book not present')
            return
        if self.libList[bookname]:
            del self.libList[bookname]
    def borrowBook(self,bookname,borrower):
        if (bookname in self.libList)==False:
            print('Book not present in Our library')
            return
        if self.libList[bookname][2]=='':
            self.libList[bookname][2]=borrower
            print('You can take that Book')
        else:
            print('You can\'t take,This Book is taken by',self.libList[bookname][2])

# a specimen of a book
# name:author,usage,borrower

print('Please Enter the name of Your Library')
libname=input()
while 1:
    myLib=library(libname,myBooks)
    print('Enter Your Choice\n1)View books in library')
    print('2)Add books in library')
    print('3)Remove book from library')
    print('4)Borrow a book from library\npress -1 for exit')
    choice=input()
    if choice=='1':
        myLib.printLibrary()
    elif choice=='2':
        print('Enter The book details in following order')
    #    name:author,usage,borrower
        print('Enter The bookname')
        bookname=input()
        print('Enter The author\'s name')
        author=input()
        print('Enter The usage')
        usage=input()
        myLib.addBook({bookname:[author,usage,'']})
    elif choice=='3':
        print('Enter The bookname')
        bookname=input()
        myLib.removeFromLib(bookname)
    elif choice=='4':
        print('Enter The bookname')
        bookname=input()
        print('Enter your name')
        borrower=input()
        myLib.borrowBook(bookname,borrower)
    elif choice=='-1':
        exit()
    else:
        print('wrong option choosed')


from  random import randint
print('Welocome to Zero kaata!!')
# take a zerokaata matrix
global zeroKaata
# variable for restarting the game
global winner
winner=-1
zeroKaata=[[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
# print the matrix
def zeroKaataPrint():
    print('******************************')
    for row in  zeroKaata:
        valueRow='|'
        for item in row:
            if (item==-1):
                valueRow+=' '
            elif(item==1):
                valueRow+='1'
            else:
                valueRow+='0'
            valueRow+='|'
        print(valueRow)
    print('******************************')

def askingName():
    global username1,username2
    print('Please Enter 1 user\'S name') 
    username1=input() 
    print('Please Enter 2 user\'S name,if You don\'t have a partner,PRESS 0')   
    username2=input()
    if username2=='0':
        username2='Computer'

def userTurn(username):
    global userInp
    if username=='Computer':
        userInp=randint(1,9)
    else:
        zeroKaataPrint()
        print(username,'\'S turn,-1 for exit')  
        userInp=input()
        if userInp=='-1':
            exit()
    # you cannot exit inside try block 
    try:
        userInp=int(userInp)
        if userInp>9 or userInp<1:
            print('Type your choice from 1-9')
            userTurn(username)
        else:
            # validating the userInp 
            # according to zerokaata
            col=userInp%3
            row=userInp//3
            if userInp%3==0:
                col=2 #to represent last item of a row
                row-=1
            else:
                col-=1
            if zeroKaata[row][col]!=-1:
                if username!='Computer':
                    print('This Box is already filled')
                userTurn(username)
            else:
                if username==username1:
                    zeroKaata[row][col]=1
                if username==username2:
                    zeroKaata[row][col]=0
                
    except :
        userTurn(username)
    
def checkWinner(username,symbol):
    #symbol is the digit by which user is playing
    # diagonal check
    global winner
    if (zeroKaata[0][0]==zeroKaata[1][1]==zeroKaata[2][2]==symbol) or (zeroKaata[0][2]==zeroKaata[1][1]==zeroKaata[2][0]==symbol) :
        print('winner is',username)
        winner=symbol
    global i
    i=0
    for row in zeroKaata:
        if (zeroKaata[i][0]==zeroKaata[i][1]==zeroKaata[i][2]==symbol) or (zeroKaata[0][i]==zeroKaata[1][i]==zeroKaata[2][i]==symbol):
            print(username,'is the Winner!!')
            winner=symbol
        i+=1
    # check for draw
    global draw
    draw=1  #initially assuming the game to be draw
    for row in zeroKaata:
        for item in row:
            if item==-1:
                # game is left
                draw=0
    if draw==1 and winner==-1:
        print('Draw Between players')
        restartGame()

# askingName()

def restartGame():
    print('Game finished, Starting a new One')
    askingName()
    global zeroKaata
    global winner
    zeroKaata=[[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
    winner=-1

# while(1):
#     userTurn(username1)#uses 1 for game
#     checkWinner(username1,1)
#     if winner!=-1:
#         #somebody won
#         #so reinitialise the values for further game
#         restartGame()
#     userTurn(username2)#uses 0 for game
#     checkWinner(username2,0)
#     if winner!=-1:
#         restartGame()


#gui work
from tkinter import *
root=Tk()
root.title('Zero Kaata by SYED')
root.geometry('500x300')
# root.maxsize('500x300')
# root.minsize('500x300')

def pressedMe():
    print('hello')
def put0(self):
    global col1Val
    
    print(col1Val)
    col1Val='1'
    col1.update()
def put1(self):
    print('hello')

#now making the gui of matrix
col1Val=StringVar()
col1Val=' '
col1=Button(root,text=col1Val)
col1.pack()
col1.bind('<Button-1>', put0)
root.mainloop()
    

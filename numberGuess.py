import random
print('I am thinking of a no. which is less than 10 \nPlease Guess it!')
while(1):
    print('If You are fed Up ,press -1')
    userNo=input()
    # now we need to handle the scenario of invalid input
    try:
        userNo=int(userNo)
    except:
        pass
    myNo=random.randrange(1,10)
    if(userNo==myNo):
        print('Whoa ,You Guessed it !!')
        exit()
    elif userNo==-1:
        exit()
    else:
        print('try Again bro/sis\nMy no. is'+str(myNo))
    

import random
# for random letter from the string
# print(random.choice('maaz'))
while(1):
    print('Welcome to SMK Password Generator \nPlease write an Expression')
    print('If You are fed Up ,press -1')
    userExp=input()
    if userExp=='-1':
        exit()
    # to allow empty user inputs
    try:
        x=[random.randint(0,9),random.randint(2,9),random.randint(2,39),random.randint(29,89),random.choice(userExp),random.choice(userExp)]
        # this shuffles the sequence passed to it and doesnot return anything
        random.shuffle(x)
        password=''
        for item in x:
            password+=str(item)
        print('Your password is')
        print(password)
    except:
        pass
    
# try contact book
# desktop notifier app
#command line program
#voice assistant
#search engine
    

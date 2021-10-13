import random

print('Lets pley')

userwin = 0
computer = 0
round = 1
i = 0

while i <= 4:
    c = random.randint(1,3)
    print('1: sang\n 2: kaqz\n, 3: qeichi\n')   
    
    user = int(input('please Enter your choice = '))
    i += 1

    if(user==1 and c==3) or (user==2 and c==1) or (user==3 and c==2):
        userwin += 1
        print("! you win !")
        print("round=", round)
    
    elif(user == c):
        print("no winner :)")
        print("round=", round)

    else:
        computer += 1
        print("! computer win !")
        print("round=", round)

    round += 1
    
    if(i == 5):
        if(userwin > computer):
            print(' Congratulations on winning this intense game ! ')
            break
        elif(userwin==computer):
            print(' this game is without a winner sorry:)')
            break
        else:
            print(' The computer won this round of the game ')
            break
import random
name=input("*****PLEASE ENTER YOUR NAME *****")
print("***** HELLO",name,"WELCOME  TO COWS AND BULLS GAME *****")
def Secretnum():
    num=list(range(10))
    random.shuffle(num)
    return num
def getsecretnum():
    number=Secretnum()
    secret_numlist=[]
    for i in range(5):
        secret_numlist.append(number[i])
    a=[]
    for i in secret_numlist:
        b=str(i)
        a.append(b)
    return a
def cowbul():
    b=getsecretnum()
    print(b)
    tries=0
    while tries<10:
        cow=0
        bull=0
        guess = int(input("Enter your guess in 5 digit : "))
        if 10000<=guess<100000:
            strguess=str(guess)
            l=[]
            for i in range(len(strguess)):
                l.append(strguess[i])
            list=[]
            for j in range(len(l)):
                if l[j] not in list:
                    list.append(l[j])
                    if l[j] in b:
                        cow=cow+1
                    if l[j]==b[j]:
                        bull=bull+1
                elif l[j] in list:
                    print("Number should not have repeated digits. Try again.")
                    break
        else:
            print("please enter 5 digit no.")
            continue
        print("cow = ",cow,"  ","bull =",bull)
        if bull==5:
            print("you win")
            break
        tries=tries+1 
    if bull!=5:
        print("you are loozer")  
        print("The real number is",b) 
cowbul()
def play_again():
    while True:
        again=input("Do you want to play again y/n")
        if again=="y":
            cowbul()
        else:
            break
play_again()
            
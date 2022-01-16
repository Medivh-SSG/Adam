n=input()
if n=="rock" or n=="paper" or n=="scissors":
    
    
    from random import randint
    c=randint(0,2)
    if c==0:
        print("rock")
    elif c==1:
        print("paper")
    elif c==2:
        print("scissors")
    a=len(n)
    b=4
    if c==0:
        b=4
    elif c==1:
        b=5
    elif c==2:
        b=8
    if a==4 and b==4:
        print("nobody win")
    elif a==5 and b==5:
        print("nobody win")
    elif a==8 and b==8:
        print("nobody win")
    elif a==4 and b==5:
        print("you lose")
    elif a==5 and b==8:
        print("you lose")
    elif a==8 and b==5:
        print("you win")
    elif a==8 and b==4:
        print("you lose")
    elif a==5 and b==4:
        print("you win")
    elif a==4 and b==8:
        print("you win")
if n!="rock" and n!="paper" and n!="scissors":
    print("error")
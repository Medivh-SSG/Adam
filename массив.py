a=int(input())
b=int(input())
j=0
k=0
mas=[[0]*b for i in range(a)]
for k in range(-1,b):
    for j in range(-1,a):
        from random import randint
        c=randint(0,100)
        mas[j-1][k-1]=c
        j=j+1
    k=k+1
print(mas)
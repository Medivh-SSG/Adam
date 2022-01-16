from random import randrange
n=int(input())
S=0
mas=[[0]*n for i in range(n)]
for k in range(-1,n):
    for j in range(-1,n):
        c=randrange(1,-2,-2)
        mas[j-1][k-1]=c
        j=j+1
    k=k+1
for k in range(0,n):
    for j in range(0,n):
        S=S+(mas[j-1][k]*mas[j-2][k])
for j in range(0,n):
    for k in range(0,n):
        S=S+(mas[j][k-1]*mas[j][k-2])
print(S)
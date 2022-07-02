m=int(input())
n=m
c=0
while n:
    c+=1
    n=n//10
a=[0]*c
s=i=d=0
n=m
while n:
    s=n%10
    a[i]=s
    i+=1
    n=n//10
for i in range(c-1,-1,-1):
    if a[i]==6:
        a[i]=9
        break
for i in range(c-1,-1,-1):
    print(a[i],end='')
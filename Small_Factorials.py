t=int(input())
f=1
while t!=0:
    n=int(input())
    for i in range(1,n+1,1):
        f=f*i
    print(f)
    f=1
    t-=1
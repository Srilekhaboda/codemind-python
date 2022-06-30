t=int(input())
k=0
while t!=0:
    n=int(input())
    for i in range(1,n,1):
        if i*i==n:
            k=1
            break
        else:
            k=0
    if k!=0:
        print("True")
    else:
        print("False")
    t-=1    
def fsum(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s=s+i
    return s
n=int(input())
k=fsum(n)
if k==n:
    print(True)
else:
    print(False)
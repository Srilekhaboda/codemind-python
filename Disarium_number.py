def count(n):
    k=0
    while n:
        d=n%10
        n//=10
        k+=1
    return k
n=int(input())    
k=count(n)
r=n
rev=0
while n:
    d=n%10
    n//=10
    rev=rev+pow(d,k)
    k-=1
if rev==r:
    print(True)
else:
    print(False)
def reverse(n):
    r=0
    while n:
        d=n%10
        n//=10
        r=r*10+d
    return r
def fun(num,m):
    k=0
    h=0
    while num:
        d=num%10
        num//=10
        k+=1
        h=h*10+d
        if k==m:
           break
    return h 
n,m=map(int,input().split())
k=reverse(n)
p=fun(n,m)
r=reverse(p)
b=fun(k,m)
print(abs(r-b))
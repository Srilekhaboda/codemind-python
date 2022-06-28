def count(n):
    c=0
    while n:
        d=n%10
        n//=10
        c+=1
    return c
def reverse(r):
    h=0
    while r:
        d=r%10
        r//=10
        h=h*10+d
    return h
n=int(input())
m=n*n
k=0
p=n
r=0
c=count(n)
while m:
    d=m%10
    m//=10
    r=r*10+d
    k+=1
    if k==c:
        break
h=reverse(r)
if h==p:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
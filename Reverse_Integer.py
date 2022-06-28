n=int(input())
r=0
if n<0:
    m=-n
else:
    m=n
while m:
    d=m%10
    m//=10
    r=r*10+d
if n>0:
    print(r)
else:
    print(-r)
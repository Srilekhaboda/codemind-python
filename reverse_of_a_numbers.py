n=int(input())
r=0
while n:
    d=n%10
    n//=10
    r=r*10+d
print(r)    
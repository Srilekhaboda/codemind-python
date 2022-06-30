n=int(input())
e=0
d=0
o=0
while n!=0:
    d=n%10
    n//=10
    if d%2==0:
        e+=1
    else:
        o+=1
if e!=0 and o==0:
    print("Even")
if e==0 and o!=0:
    print("Odd")
if e!=0 and o!=0:
    print("Mixed")
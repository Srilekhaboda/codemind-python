def gcd(a,b):
    if b>a:
        return gcd(b,a)
    elif b==0:
        return a
    else:
        return gcd(b,a%b)
t=int(input())
for i in range(t):
    n,a,b,k=map(int,input().split())
    g=gcd(a,b)
    lcm=(a*b)//gcd(a,b)
    tab=n//lcm
    ta=n//a-tab
    tb=n//b-tab
    if ta+tb>=k:
        print("Win")
    else:
        print("Lose")
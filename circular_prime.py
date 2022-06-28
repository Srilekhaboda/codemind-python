def prime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    else:
        return True
n=int(input())
m=n
r=0
while n:
    d=n%10
    n//=10
    r=r*10+d
if prime(m) and prime(r):
    print("circular prime")
if prime(m):
    if prime(r)==0:
        print("prime but not a circular prime")
else:
    print('not prime')
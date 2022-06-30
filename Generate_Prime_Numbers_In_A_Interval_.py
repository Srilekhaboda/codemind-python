def prime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    else:
        return True
n=int(input())
m=int(input())
if n==1:
    n=2
for i in range(n,m+1):
    if prime(i):
        print(i)
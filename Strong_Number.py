def factorial(n):
    k=1
    while n:
        k=k*n
        n-=1
    return k
n=int(input())
m=n
s=0
while n:
    d=n%10
    n//=10
    k=factorial(d)
    s=s+k
if s==m:
    print('The number',m,'is a strong number')
else:
    print('The number',m,'is not a strong number')
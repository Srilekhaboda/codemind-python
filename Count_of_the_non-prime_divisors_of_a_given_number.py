def isprime(num):
    p=0
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return 0
    else:
        return 1
n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        k=isprime(i)
        if k==0:
            c+=1
print(c+1)            
n=int(input())
k=0
while n:
    d=n%10
    n//=10
    if k<d:
        k=d
print(k)        
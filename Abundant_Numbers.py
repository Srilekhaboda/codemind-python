def factsum(n):
    m=0
    for i in range(1,n):
        if n%i==0:
            m=m+i
    return m
n=int(input())
m=factsum(n)
if m>n:
    print(True)
else:
    print(False)
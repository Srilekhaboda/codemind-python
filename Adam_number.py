def reverse(num):
    r=0
    while num:
        d=num%10
        num//=10
        r=r*10+d
    return r
n=int(input())
m=n
s=n*n
k=reverse(m)
p=k*k
h=reverse(p)
if h==s:
    print(True)
else:
    print(False)
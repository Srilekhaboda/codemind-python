def digitsum(n):
    s=0
    while n:
        d=n%10
        n//=10
        s=s+d
    return s
n=int(input())
while n>9:
    s=digitsum(n)
    if s>9:
        n=s
    else:
        print(s)
        break
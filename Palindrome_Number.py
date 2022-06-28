def palindrome(m):
    k=m
    r=0
    while m:
        d=m%10
        m//=10
        r=r*10+d
    if r==k:
        print(True)
    else:
        print(False)
n=int(input())
while n:
    m=int(input())
    palindrome(m)
    n-=1
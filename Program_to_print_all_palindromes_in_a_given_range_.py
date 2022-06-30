def palindrome(num):
    k=num
    r=0
    while num:
        d=num%10
        num//=10
        r=r*10+d
    if r==k:
        return 1
    else:
        return 0
n=int(input())
m=int(input())
for i in range(n,m):
    if palindrome(i):
        print(i,end=' ')
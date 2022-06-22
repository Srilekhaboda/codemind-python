n=int(input())
a=n
r=0
while n:
    rem=n%10
    r=r*10+rem
    n=n//10
if a==r:
    print(True)
else:
    print(False)
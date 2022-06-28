n=int(input())
s=0
p=1
while n!=0:
    d=n%10
    n//=10
    s=s+d
    p=p*d
if s==p:
    print('Spy Number')
else:
    print('Not Spy Number')
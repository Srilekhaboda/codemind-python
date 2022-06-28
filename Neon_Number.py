n=int(input())
m=n*n
s=0
while m!=0:
    d=m%10
    m//=10
    s=s+d
if s==n:
    print('Neon Number')
else:
    print('Not Neon Number')
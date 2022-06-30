x=int(input())
c=0
r=0
while(x>0):
    d=x%10
    x=x//10
    c+=1
    r=r*10+d
if c==10:
    k=r%10
    r=r//10
    if k==0:
        print('Invalid')
    else:
        print('Valid')
else:
    print('Invalid')
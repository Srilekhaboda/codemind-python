a,b=map(int,input().split())
if a>b:
    a,b=b,a
if b==a+1:
    #print(a,b)
    print('Yes')
else:
    if a==1 and b==10:
        print('Yes')
    else:
        print('No')
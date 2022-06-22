a,b=map(int,input().split())
c=a+b*2
if(c%2!=0 or (a%2!=0 and b==0) or (a==0 and b%2!=0)):
    print("NO")
else:
    print("YES")
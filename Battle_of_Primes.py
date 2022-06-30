def prime(a):
    c=0
    if a!=1:
        for i in range(2,a):
            if(a%i)==0:
                c=1
                break
    if c==0:
        return 0
    else:
        return 1
n=int(input())
m=int(input())
s=n+m+1
c=1
while prime(s):
    s+=1
    c+=1
print(c)
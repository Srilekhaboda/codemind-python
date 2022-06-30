n=int(input())
a=[]
k=n
t=f=0
while k:
    t=k%10
    a.append(t)
    k=k//10
for i in range(len(a)):
    for j in range(len(a)):
        if i!=j:
            if a[i]==a[j]:
                f=1
                break
if f==0:
    print('Unique Number')
else:
    print('Not Unique Number')
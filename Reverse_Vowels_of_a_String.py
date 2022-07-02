a=input()
test="aeiouAEIOU"
c=0
s=[]
k=[]
for i in range(len(a)-1,-1,-1):
    if a[i]in test:
        s.append(a[i])
for i in range(len(a)):
    if a[i] in test:
        k.append(s[c])
        c+=1
    else:
        k.append(a[i])
f="".join(k)
print(f)
def fib(a):
    if a<=1:
        return a
    return fib(a-1)+fib(a-2)
n= int(input())
d=[0]*n
j=s=0
for i in range(n):
    if d[i-1] <n:
        d[i]=fib(i)
    else:
        break
    j+=1
mx=d[j-1]
mi=d[j-2]
if n-mx<mi-n:
    print(mi)
elif n-mx>mi-n:
    print(mx)
elif n-mx==mi-n:
    print(mi,mx)
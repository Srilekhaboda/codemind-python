def sum_pd(num):
    k=0
    for i in range(1,num):
        if num%i==0:
            k=k+i
    return k
n=int(input())
m=int(input())
a=sum_pd(n)
b=sum_pd(m)
if a==m and b==n:
    print("Amicable")
else:
    print("Not Amicable")
n=int(input())
for i in range(64+n,64,-1):
    for j in range(1,n+1,1):
        print(chr(i),end=" ")
    n-=1
    print()
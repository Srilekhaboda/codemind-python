x=int(input())
c=0
for i in range(x):
    z=input()
    for j in range(len(z)):
        if z[j] in '1234567890':
            print("Yes")
            break
    else:
        print("No")
t=int(input())
while t:
    s=input()
    flag=0
    for i in s:
        if i.isdigit():
            continue
        else:
            flag=1
            break
    if flag==0:
        print("True")
    else:
        print("False")
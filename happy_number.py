def hp(a):
    t=k=0
    while a:
        t=a%10
        k=k+(t**2)
        a=a//10
    return k
n=int(input())
k=n
while 1:
    if hp(k)>1 and hp(k)<10:
        print("False")
        break
    elif hp(k)==1:
        print("True")
        break
    else:
        k=hp(k)
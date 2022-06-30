x=input()
c=0
for i in x:
    if i.isdigit():
        c+=1
if(c==0):
    print("Doesn't contain digit")
else:
    print("Contains {0} digit".format(c))
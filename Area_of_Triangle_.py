a,b,c=map(int,input().split())
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))
import math
print("{:.2f}".format(math.sqrt(area)))
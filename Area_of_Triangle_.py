import math
A,B,C=map(int,input().split())
S=(A+B+C)/2
area=math.sqrt(S*(S-A)*(S-B)*(S-C))
print("%0.2f"%area)
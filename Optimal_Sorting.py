a = int(input())
while(a):
    b=int(input())
    s=list(map(int,input().split()))
    b=sorted(s)
    if(s==b):
        print(0)
    else:
        print(max(b)-min(b))
    a-=1
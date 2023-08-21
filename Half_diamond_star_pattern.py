N = int(input())
if(N >= 3 and N <=100):
        
    for i in range(1 , N + 1):
        print("*" * i)
    for i in range(N-1 , 0 , -1):
        print("*" * i)
else:
    print("The pattern is not possible")
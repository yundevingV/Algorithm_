import sys

n = int(sys.stdin.readline())


for _ in range(n) :
    x = int(sys.stdin.readline())
    d = [0] *(x+1)
    
    if x == 1 :
        print(1)
    elif x ==2 :
        print(2)
    elif x == 3 :
        print(4)
    else :
        for i in range(4,x+1) :
            d[1] = 1
            d[2] = 2
            d[3] = 4
            d[i] = d[i-3] + d[i-2] + d[i-1] 
        print(d[x])


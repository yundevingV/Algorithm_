import sys

n = int(sys.stdin.readline())

for _ in range(n) :
    t = int(sys.stdin.readline())
    d = [0] * (t+1)

    for i in range(1,t+1) :
        if i == 1 or i == 2 or i == 3 :
            d[i] = 1
        else :  
            d[i] = d[i-2] + d[i-3]
    print(d[t])


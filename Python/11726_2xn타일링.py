import sys

x = int(sys.stdin.readline())

d = [0] * (x+1)


for i in range(1,x+1) :
    if i == 1 :
        d[1] = 1 
    elif i == 2 :
        d[2] = 2
    else : 
        d[i] = (d[i-1] + d[i-2]) % 10007


print(d[x])
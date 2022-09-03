import sys

x = int(sys.stdin.readline())

d = [0] * (x+1)

d[0] = 0
d[1] = 1
d[2] = 3 

for i in range(3,x+1) :
    d[i] = (d[i-1] + 2*d[i-2]) % 10007

print(d[x])
import sys


n = int(sys.stdin.readline())

d = [1] * (n+1)

lst = list(map(int, sys.stdin.readline().split()))

for i in range(1,n) :
    for j in range(0,i) :
        if lst[i] > lst[j] :
            d[i] = max(d[i], d[j] +1)

print(max(d))
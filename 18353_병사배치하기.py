import sys

n = int(sys.stdin.readline())

d = [1] * (n+1)

lst = list(map(int, sys.stdin.readline().split()))

for i in range(n-1) :
    if lst[i] > lst[i+1] : 
        d[i] = max(d[i], d[i+1] + 1 + d[i])
    else :
        d[i] = max(d[i], d[i-1])

print(d)
print(len(lst) - max(d))
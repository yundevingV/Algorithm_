import sys

n = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split()))


d = [-1001] *100001
d[1] = lst[0]
for i in range(2,n+1) :
    d[i] = max(lst[i-1] , lst[i-1] + d[i-1])

print(max(d))
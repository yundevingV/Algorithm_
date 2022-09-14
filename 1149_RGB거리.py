import sys

n = int(sys.stdin.readline())

g = []

for i in range(n) :
    s = list(map(int, sys.stdin.readline().split()))
    g.append(s)

#빨강 초록 파랑으로 다 칠해줘야함

for i in range(1,n) :
    g[i][0] = min(g[i-1][1] , g[i-1][2]) + g[i][0]
    g[i][1] = min(g[i-1][0] , g[i-1][2]) + g[i][1]
    g[i][2] = min(g[i-1][1] , g[i-1][0]) + g[i][2]

print(g)
print(min(g[n-1]))
    
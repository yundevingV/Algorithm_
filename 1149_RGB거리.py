import sys

n = int(sys.stdin.readline())

d = [[0] * (n) for _ in range(n)]

g = []

for i in range(n) :
    s = list(map(int, sys.stdin.readline().split()))
    g.append(s)


print(g)
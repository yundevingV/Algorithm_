import sys


n = int(sys.stdin.readline())
g = list(map(int, sys.stdin.readline().split()))


for i in sorted(list(set(g))) :
    print(i,end=' ')


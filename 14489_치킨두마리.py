import sys

n,m = map(int, sys.stdin.readline().split())

c = int(sys.stdin.readline())

if n+m >= c*2 :
    print(n+m-c*2)
else :
    print(n+m)
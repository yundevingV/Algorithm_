import sys
import math 

n = int(sys.stdin.readline())

for i in range(n) :
    a,b = map(int, sys.stdin.readline().split())
    print(math.lcm(a,b))

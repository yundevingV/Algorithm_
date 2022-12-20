import sys
import math

n,m = map(int, sys.stdin.readline().split())

print(math.gcd(n,m))
print(math.lcm(n,m))

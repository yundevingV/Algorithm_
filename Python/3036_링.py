import sys
import math

n = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split()))

p = lst[0]

for i in range(1,n) :
    gcdNumber = math.gcd(p,lst[i])
    
    print(p//gcdNumber,end='')
    print('/',end='')
    print(lst[i]//gcdNumber,end='\n')

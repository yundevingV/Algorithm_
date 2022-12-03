import sys
import math

n, m = map(int, sys.stdin.readline().split())
i=0
while True :
    i+=1
    
    if (i/n) - (i/m) >= 1 :
        break


print(math.ceil((i/n)))
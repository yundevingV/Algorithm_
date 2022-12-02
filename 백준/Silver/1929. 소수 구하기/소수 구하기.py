import sys
import math
n1,n2 = map(int, sys.stdin.readline().split())


for i in range(n1,n2+1) :
    c = 0
    
    for j in range(2, int(math.sqrt(i)) + 1) :
        
        
        if i % j == 0 :
            c+=1
            break
    if c == 0 and i > 1 :
        print(i)
        pass

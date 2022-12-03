import sys
import math

n=1

while n != 0 :
    n = int(sys.stdin.readline())
    k=0
    for i in range(n+1,(2*n)+1) :
        c=0
        
        for j in range(2, int(math.sqrt(i)) + 1) :
            if i % j == 0 :
                # 소수가아니면
                c+=1
                break
        if c == 0 and i > 1 :
            k+=1
            
            pass
    if n !=0  :
        print(k)


import sys
import math

t = int(sys.stdin.readline())

for i in range(t) :
    test = []
    lst = []
    n = int(sys.stdin.readline())
    
    for j in range(2,n+1) :
        c=0
        
        for jj in range(2, int(math.sqrt(j) + 1)) :
            if j % jj == 0 :
                # 소수가아니면
                c+=1
                break
        if c == 0 and j > 1 :       
            test.append(j)
            pass
    
    for i in test :
        ya = n - i
        if ya in test :
            lst.append(i)

    printNum = len(lst)//2

    if len(lst) % 2 == 1 :
        print(lst[printNum],lst[printNum])
    else :
        print(lst[printNum-1],lst[printNum])
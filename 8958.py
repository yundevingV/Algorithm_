from re import L
import sys

num = int(sys.stdin.readline())


for i in range(num) :
    str = (sys.stdin.readline().strip())
    v=0
    sum=0
    for j in str :
        if j =='O' :
            v+=1
            sum+=v
        else :
            v=0
    print(sum)


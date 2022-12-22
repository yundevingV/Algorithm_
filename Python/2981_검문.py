import sys
import math

n = int(sys.stdin.readline())

lst = [] 

for i in range(n) :
    a = int(sys.stdin.readline())
    lst.append(a)

lst.sort()

gc = []

for i in range(len(lst)-1) :
    gc.append(lst[i+1] - lst[i])

gc.sort()
mini = gc[0]

for i in range(len(gc)-1) :
    mini = math.gcd(mini,gc[i+1])

result = []

for i in range(2,int(math.sqrt(mini)+1)) :
    if mini % i == 0 : 
        result.append(i)
        if ((i**2) != mini) :
            result.append(mini//i)

result.append(mini)

result.sort() 

for i in result :
    print(i,end=' ')
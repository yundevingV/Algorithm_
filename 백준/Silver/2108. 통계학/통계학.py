import sys
from collections import Counter

n = int(sys.stdin.readline())

lst = []

for i in range(n) :
    num = int(sys.stdin.readline())
    lst.append(num)

lst.sort()

print(round(sum(lst)/n))

middleIndex = n // 2 
print(lst[middleIndex])

chlqls = Counter(lst).most_common()

if len(chlqls) > 1 :
    if chlqls[0][1] == chlqls[1][1] :
        print(chlqls[1][0])
    else :
        print(chlqls[0][0])
else :
    print(chlqls[0][0])

print(max(lst) - min(lst))

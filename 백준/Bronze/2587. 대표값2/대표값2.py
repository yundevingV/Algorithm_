import sys

lst = []
for i in range(5) :
    n = int(sys.stdin.readline())
    lst.append(n)
lst.sort()
print(int(sum(lst)/5))
print(lst[2])


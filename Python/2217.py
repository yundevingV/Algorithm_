import sys

n = int(sys.stdin.readline())
lst = []
for _ in range(n) :
    x = int(sys.stdin.readline())
    lst.append(x)

lst.sort()
r=[]
for i in range(len(lst)) :
    a = lst[i] * (len(lst)-i)
    r.append(a)
print(max(r))

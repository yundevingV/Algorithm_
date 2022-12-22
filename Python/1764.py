import sys

n,m = [int(x) for x in sys.stdin.readline().split()]

lst1 = set()
lst2 = set()
for i in range(n) :
    a = sys.stdin.readline().rstrip()
    lst1.add(a)

for j in range(m) :
    a = sys.stdin.readline().rstrip()
    lst2.add(a)


result = sorted(lst1 & lst2)


print(len(result))
for i in result :
    print(i)
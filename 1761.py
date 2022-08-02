import sys

n,m = [int(x) for x in sys.stdin.readline().split()]

lst1 = []
lst2 = []
for i in range(n) :
    a = sys.stdin.readline().rstrip()
    lst1.append(a)

for j in range(m) :
    a = sys.stdin.readline().rstrip()
    lst2.append(a)
r=[]
c=0
for i in lst1 :
    for j in lst2 :
        if i == j :
            r.append(i)
            c+=1

r.sort()
r= set(r)
print(len(r))
for i in r :
    print(i)

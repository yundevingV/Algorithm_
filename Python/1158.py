import sys
n,k = map(int, sys.stdin.readline().split())

q =[]

pop=0
a = k-1

r=[]
for i in range(n) :
    q.append(i+1)

while q :
    pop = (pop + a) % len(q)
    r.append(q.pop(pop))

print('<' + ', '.join(list(map(str,r)))+'>')
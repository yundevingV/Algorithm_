import sys

n,m,k = [int(x) for x in sys.stdin.readline().split()]


m1=[]
k1=[]
dict = {}
for i in range(k) :
    i,j = [int(x) for x in sys.stdin.readline().split()]
    m1.append(i)
    k1.append(j)

print(m1)
print(k1)
sum=0
for i in m1 :
    sum+=i
    if sum >= m :
        print(sum)
        

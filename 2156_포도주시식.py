import sys

n = int(sys.stdin.readline())

d = [0] * (n+1)

lst = []

for _ in range(n) :
    x = int(sys.stdin.readline())
    lst.append(x)



for i in range(3,n) :
    d[0] = lst[0]
    d[1] = lst[1]
    d[2] = lst[2]
    d[i] = max(d[i-3] + d[i-2] , d[i-2] + lst[i] , d[i-3])

print(d) 
    
print(max(d)) 

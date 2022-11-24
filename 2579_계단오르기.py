import sys

n = int(sys.stdin.readline())

d = [0] * (301)

v = [0] *(301)

for i in range(n) :
    m = int(sys.stdin.readline())
    v[i]=m

d[0] = v[0]
d[1] = v[0] + v[1]
d[2] = max(v[2] +v[0],v[2]+v[1])

for i in range(3,n) :
    d[i] = max(d[i-3] + v[i-1] + v[i] , d[i-2] + v[i])

print(d[n-1])

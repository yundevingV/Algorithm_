import sys

n = int(sys.stdin.readline())

d = [0] * (10001)

# lst = [0] * (10001)

# for i in range(n) :
#     x = int(sys.stdin.readline())
#     lst[i] = x

lst = []

for i in range(n) :
    x = int(sys.stdin.readline())
    lst.append(x)

d[0] = lst[0]
d[1] = lst[1] + lst[0]
d[2] = max(lst[2] + lst[0] , lst[2]+lst[1], d[1])

for i in range(3,n) :
    d[i] = max(lst[i]+d[i-2] , d[i-3] + lst[i-1] + lst[i] , d[i-1] )

    
print(max(d)) 

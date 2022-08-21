import sys
import heapq

n = int(sys.stdin.readline())

h=[]

for _ in range(n) :
    i = int(sys.stdin.readline())
    heapq.heappush(h,i)


result = 0

while len(h) > 1 :
    s=0
    for i in range(2) :
        x = heapq.heappop(h)
        s+=x
    result+=s

    heapq.heappush(h,s)


print(result)

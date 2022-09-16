import heapq
import sys

h = []
n = int(sys.stdin.readline())

for _ in range(n) :
    x = int(sys.stdin.readline())
    if h :
        if x == 0 :
            print(-heapq.heappop(h))
        else :
            heapq.heappush(h,-x)
    else :
        if x == 0 :
            print(0)
        else :
            heapq.heappush(h,-x)

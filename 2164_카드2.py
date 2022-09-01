import sys
from collections import deque

n = int(sys.stdin.readline())

q = deque()

for i in range(n) :
    q.append(i+1)

i = 0

while len(q) > 1 :
    if i % 2 == 0 :
        q.popleft()
    else :
        x = q.popleft()
        q.append(x)
    i+=1

print(q[0])



import sys
from collections import deque

n , m , k, x = map(int, sys.stdin.readline().split())

v = [False] * (n+1)
graph = [[] for _ in range(n+1)]

for i in range(m) :
    a,b=map(int, sys.stdin.readline().split())
    graph[a].append(b)

d = [0] * (n+1)

def bfs(x,v,d) :
    queue = deque()
    queue.append(x)
    v[x] = True
    while queue :
        x = queue.popleft()
        for i in graph[x] :
            if v[i] != True :
                d[i]= d[x]+1
                queue.append(i)
                v[i] = True

bfs(x,v,d)
if k not in d :
    print('-1')
else :
    for i in range(len(d)) :
        if d[i] == k :
            print(i)

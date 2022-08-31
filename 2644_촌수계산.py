from collections import deque
import sys


n = int(sys.stdin.readline())
#사람 수 

a,b = map(int, sys.stdin.readline().split())

visited = [-1] * (n+1)
graph = [[] for _ in range(n+1)]

att = int(sys.stdin.readline())


for _ in range(att) :
    n,m = map(int, sys.stdin.readline().split())
    graph[n].append(m)
    graph[m].append(n)
    


def bfs(a) :
    q = deque()
    q.append(a)
    visited[a] = 0
    while q :
        x = q.popleft()
        for i in graph[x] :
            if visited[i] == -1 :
                visited[i] = visited[x] + 1 
                q.append(i)

bfs(a)



print(visited[b])
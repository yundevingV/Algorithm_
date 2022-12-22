from collections import deque
import sys
n,m = map(int, sys.stdin.readline().split())
#n은 정점 , m은 간선갯수

visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m) :
    u,v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

cnt  =0
def bfs(ii) :
    q = deque()
    q.append((ii))
    visited[ii] = True
    while q :
        x = q.popleft()
        for i in graph[x] :
            if visited[i] == False :
                visited[i] = True
                q.append(i)


for i in range(1,len(graph)) :
    if visited[i] == False :
        bfs(i)
        cnt +=1

print(cnt)


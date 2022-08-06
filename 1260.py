import sys
from collections import deque
n , m , v = map(int, sys.stdin.readline().split())

visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]

for i in range(m) :
    a,b=map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1) :
    graph[i].sort()
# 낮은순서부터 방문해서 솔트..

def dfs(graph,v,visited) :
    visited[v] = True 
    print(v,end=' ')
    
    for i in graph[v] :
       if not visited[i] :
           dfs(graph,i,visited)

dfs(graph,v,visited)

sv=[False] *(n+1)
def bfs(graph,v,visited) :
    queue = deque([v])
    visited[v] = True
    while queue :
        v = queue.popleft()
        print(v,end=' ')
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True
print()
bfs(graph,v,sv)                




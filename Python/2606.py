import sys
from collections import deque
n  = int(input())
m  = int(input())

visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]
c=0

for i in range(m) :
    a,b=map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1) :
    graph[i].sort()
# 낮은순서부터 방문해서 솔트..
def dfs(graph,v,visited) :
    global c
    visited[v] = True 
    
    for i in graph[v] :
       if not visited[i] :
           dfs(graph,i,visited)
           c+=1

dfs(graph,1,visited)

print(c)
            




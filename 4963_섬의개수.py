#https://www.acmicpc.net/problem/4963

import sys
from collections import deque

n=100
m=100

dx=[1,-1,0,0,1,-1,1,-1]
dy=[0,0,1,-1,-1,1,1,-1]

def bfs(i,j,visited) :
    q=deque()
    q.append((i,j))
    visited[i][j] = True

    while q :
        x,y = q.popleft()
        for i in range(8) :
            nx = x +dx[i]
            ny = y +dy[i]
            if 0 <= nx < m and 0 <= ny < n : 
                if visited[nx][ny] == False and graph[nx][ny] == 1 :
                    q.append((nx,ny))
                    visited[nx][ny] = True



result=[]

while n !=0 and m != 0 :
    n,m = map(int, sys.stdin.readline().split())
    graph=[]
    cnt =0
    
    for i in range(m) :
        graph.append(list(map(int, sys.stdin.readline().split())))
    visited = [[False] *n for _ in range(m)]

    for k in range(m) :
        for j in range(n) :
            if graph[k][j] == 1 and visited[k][j] == False:
                bfs(k,j,visited)
                cnt+=1
    if n !=0 and m != 0 :
        result.append(cnt)

for i in result :
    print(i)

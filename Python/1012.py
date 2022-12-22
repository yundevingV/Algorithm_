from collections import deque
import sys


num= int(input())


dx = [0,0,1,-1]
dy = [1,-1,0,0]


def bfs(x,y,graph) :
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
    while queue :
        x,y = queue.popleft()

        for a in range(4) :
            nx = x +dx[a]
            ny = y +dy[a]
            if nx < 0 or ny < 0 or nx >= m or ny >= n :
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0 
                queue.append((nx,ny))

for i in range(num) :
    c=0

    m,n,k = map(int, sys.stdin.readline().split())
    graph =[[0]*n for _ in range(m) ]
    #세로 곱하기 가로 !!
    for _ in range(k) :
        a,b = map(int, sys.stdin.readline().split())
        graph[a][b]=1

    for i in range(m) :
        for j in range(n) :
            if graph[i][j] == 1 :
                bfs(i,j,graph)
                c+=1
    print(c)


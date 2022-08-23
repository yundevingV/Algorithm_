import sys
from collections import deque

h = int(sys.stdin.readline())

# h보다 낮으면 는 범람하는 위치

graph = []

num = 0

for i in range(h) :
    graph.append(list(map(int, sys.stdin.readline().split())))
    for j in range(h) :
        if num < graph[i][j] :
            num = graph[i][j]


dx=[1,-1,0,0]
dy=[0,0,1,-1]


result = 0
cnt = 0


def qqq(x,y,k,visited) :
    global cnt
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    while q :

        x,y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < h :
                if graph[nx][ny] > k and visited[nx][ny] == False :
                    visited[nx][ny] = True 
                    q.append((nx,ny))

for k in range(num) :
    visited = [[False] * (h) for _ in range(h)]
    cnt =0

    for i in range(h) :
        for j in range(h) :
            if visited[i][j] == False and graph[i][j] > k:
                qqq(i,j,k,visited)
                cnt +=1 

    if result < cnt :
        result = cnt

print(result)
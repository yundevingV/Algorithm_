import sys
from collections import deque

n,m,h = map(int, sys.stdin.readline().split())


graph=[]

for _ in range(h) :
    for i in range(m) :
        graph.append(list(map(int, sys.stdin.readline().split())))


dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]


def bfs() :
    q = deque()
    for i in range(m*h) :
        for j in range(n) :
            if graph[i][j] == 1 :
                q.append((i,j))
    
    while q :
        x,y = q.popleft()
        for k in range(4) :
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < m*h and 0 <= ny < n :
                if graph[nx][ny] == 0 :
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx,ny))
                elif graph[nx][ny] == -1 :
                    continue
        print(graph)

bfs()

answ=0
pivot = 0

for i in range(m*h) :
    for j in range(n) :
        if graph[i][j] == 0 :
            pivot +=1
            break        
        else :
            answ = max(answ,graph[i][j])

if pivot > 0 :
    print(-1)
else :
    print(answ-1)



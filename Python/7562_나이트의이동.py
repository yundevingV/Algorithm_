from re import L
import sys
from collections import deque

n = int(sys.stdin.readline())

dx = [1,1,2,2,-1,-1,-2,-2]
dy = [2,-2,1,-1,2,-2,1,-1]

def bfs(x,y,v) :
    q = deque()
    q.append((x,y))
    v[x][y] = True
    while q :
        x,y = q.popleft()
        for i in range(8) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l :
                if v[nx][ny] == False :
                    graph[nx][ny] = graph[x][y] +1
                    q.append((nx,ny))
                    v[nx][ny] = True



for i in range(n) :
    l = int(sys.stdin.readline())
    graph = [[0] * l for _ in range(l)]
    v = [[False] * l for _ in range(l)]
    x,y = map(int, sys.stdin.readline().split())
    graph[x][y] = 0
    targetX , targetY = map(int, sys.stdin.readline().split())
    bfs(x,y,v)
    print(graph[targetX][targetY])





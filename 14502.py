from collections import deque
import sys
import copy

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n,m = map(int, sys.stdin.readline().split())
graph=[]

for i in range(n) :
    graph.append(list(map(int, sys.stdin.readline().split())))

final = 0
def bfs() :
    global final
    result=0
    queue = deque()
    a=copy.deepcopy(graph)
    for i in range(n) :
        for j in range(m) :
            if a[i][j] == 2 :
                queue.append((i,j))
    while queue :
        x,y = queue.popleft()
        for k in range(4) :
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m :   
                if a[nx][ny] == 0 :
                    a[nx][ny] = 2
                    queue.append((nx,ny))

    for i in range(n) :
        for j in range(m) :
            if a[i][j] == 0 :
                result +=1
    
    final = max(result,final)

def qur(c) :
    if c == 3:
        bfs()
        return
    for i in range(n) :
        for j in range(m) :
            if graph[i][j] == 0 :
                graph[i][j] = 1 
                qur(c+1)
                graph[i][j] = 0

qur(0)

print(final)
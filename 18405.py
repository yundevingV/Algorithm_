import sys
from collections import deque

n,k = map(int, sys.stdin.readline().split())
graph=[]

for i in range(n) :
    graph.append(list(map(int, sys.stdin.readline().split())))

s,x,y = map(int, sys.stdin.readline().split())
# s 초후 xy 좌표에ㅐ 있는 바이러스.
# s를 그냥 함수실행횟수라고 생각.

dx = [1,-1,0,0]
dy = [0,0,1,-1]
lst =[]

for i in range(n) :
    for j in range(n) :
        if graph[i][j] != 0 :
            lst.append((graph[i][j],i,j))

def bfs(s) :
    c=0
    lst.sort()    
    q = deque(lst)

    while q :
        if s == c :
            break
        for _ in range(len(q)) :
            r,x,y = q.popleft()

            for v in range(4) :
                nx = x + dx[v]
                ny = y + dy[v]
                if 0 <= nx < n and 0 <= ny <n :
                    if graph[nx][ny] == 0 :
                        graph[nx][ny] = r
                        q.append((graph[nx][ny],nx,ny))
        c+=1
bfs(s)

print(graph[x-1][y-1])

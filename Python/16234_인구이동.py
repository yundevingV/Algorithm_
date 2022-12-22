import sys
from collections import deque

n,l,r = map(int, sys.stdin.readline().split())
# n은 땅크기
#두나라 인구 차이가 l <= 인구차이 <= R

graph =[[] *n for _ in range(n)]
lst=[]
resultLst=[]

for i in range(n) :
    a = list(map(int, sys.stdin.readline().split()))
    graph[i]= a

dx=[1,-1,0,0]
dy=[0,0,1,-1]


def bound(x,y,q) :
    for k in range(4) :
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < n  :
            if l <= abs(graph[x][y] - graph[nx][ny]) <= r  and visited[nx][ny] == False:
                q.append((nx,ny))
                lst.append((nx,ny))
                resultLst.append(graph[nx][ny])
                visited[nx][ny] = True
            


def bfs(x,y) :
    global lst,resultLst

    lst = []
    resultLst=[]

    q= deque()
    q.append((x,y))
    visited[x][y] = True

    lst.append((x,y))
    resultLst.append(graph[x][y])

    while q :
        x,y = q.popleft()
        bound(x,y,q)
    

cnt =0 


while True:
    
    visited = [[False] * (n) for _ in range(n)]
    end = True

    for i in range(n) :
        for j in range(n) :
            if visited[i][j] == False :
                bfs(i,j)
                visited[i][j] = True
                #국경 열면 True
                if len(resultLst) > 1 :
                    end = False
                    result = sum(resultLst) // len(resultLst)
                    for x,y in lst :
                        graph[x][y] = result
    if end == True:
        break 

    cnt +=1


print(cnt)

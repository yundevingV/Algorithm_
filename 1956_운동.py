import sys

INF = int(1e9)

n,m = map(int,sys.stdin.readline().split())

graph = [[INF]*(n+1) for _ in range(n+1)]


for _ in range(m) :
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = c


for k in range(1,n+1) :
    for i in range(1,n+1) :
        for j in range(1,n+1) :
            graph[i][j] = min(graph[i][j] , graph[i][k] + graph[k][j])


result = INF 

#[1][1] [2][2] [3][3] 이런식으로 존재해야 다시 왓다가 돌아가는 사이클 완성
for i in range(n) :
    result = min(result , graph[i][i])



if result == INF :
    print(-1)
else :
    print(result)


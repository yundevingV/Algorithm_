import sys
input = sys.stdin.readline

INF = int(1e9)

#n은 도시의개수 m은 노선의 갯수
n,m = map(int, input().split())

edges = []

distance = [INF] * (n+1)

for _ in range(m) :
    a, b, c = map(int, input().split())
    edges.append((a,b,c))

def bellmanFord(start) :
    distance[start] = 0
    
    for i in range(n) :
        for cur,nextNode,cost in edges :
            if distance[cur] != INF and distance[nextNode] > distance[cur] + cost :
                distance[nextNode] = distance[cur] + cost
                if i == n-1 :
                    return True
    return False

startNode = 1

negative_cycle = bellmanFord(startNode) 



if negative_cycle :
    print('-1')
else : 
    for i in range(startNode+1,len(distance),1) :
        if distance[i] == INF :
            print('-1')
        else :
            print(distance[i])




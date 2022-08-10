import sys


num= int(input())

# def d(graph,v,k) :
#     for j in range(k) :

#     v[v] = True 
#     for i in graph[v] :
#         if v[v] == False :


for i in range(num) :
    m,n,k = map(int, sys.stdin.readline().split())
    graph =[[] for _ in range(m+1) ]
    
    for _ in range(k) :
        a,b = map(int, sys.stdin.readline().split())
        graph[a][b]=1

    for j in range(m) :
        print(graph[j])
    



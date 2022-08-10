#깊이우선 dfs 로 푸는것이 유용하다
# 가로 -> 세로

n  = int(input())

graph=[]

count =[]
v=0
for i in range(n) :
    graph.append(list(map(int, input())))
def dfs(x,y) :
    global v
    
    # 충돌할경우
    if x <= -1 or y <= -1 or x >= n or y >= n :
        return False
    if graph[x][y] == 1 :
        v+=1
        graph[x][y] = 0
        
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    
    return False

c=0
r=[]
for i in range(n) :
    for j in range(n) :
        if dfs(i,j) == True :
            r.append(v)
            c +=1
            v=0

print(c)

r.sort()

for i in r :
    print(i)


def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for i in range(n) :
        if visited[i] == False :
            dfs(n,computers,visited,i)
            answer += 1
    return answer

def dfs(n,computers,visited,idx) :
    # 방문처리
    visited[idx] = True    
    for i in range(n) :
        # 다른 컴퓨터이자 연결된 컴퓨터
        if i != idx and computers[idx][i] == 1 :
            # 방문을 하지 않은 컴퓨터
            if not visited[i] :
                dfs(n,computers,visited,i)
    
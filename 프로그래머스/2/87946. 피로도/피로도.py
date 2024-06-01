answer = 0
def DFS(k,count,dungeons,check) :
    global answer;
    answer = max(answer,count);
    
    for i in range(len(dungeons)) :
        # 방문하지 않고 최소 피로도 보다 높을때 방문
        if check[i] == 0 and k >= dungeons[i][0] :
            # 방문완료
            check[i] = 1;
            
            DFS(k-dungeons[i][1],count + 1,dungeons,check);
            check[i] = 0;
        
    
def solution(k, dungeons):
    global answer;
    
    # 방문 했는지 안했는지 체크하는 배열
    check = [0] * len(dungeons);
    
    # 탐색 시작
    DFS(k,0,dungeons,check)

            
    return answer
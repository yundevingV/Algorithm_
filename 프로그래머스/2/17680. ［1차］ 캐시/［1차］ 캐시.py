from collections import deque


def solution(cacheSize, cities):
    answer = 0;

    # 큐 생성
    q = deque();

    for i in cities : 
        i = i.lower();
        # 이미 존재할때 삭제하고 새로 삽입
        if cacheSize == 0 :
            return len(cities) * 5;
        if i in q :
            q.remove(i);
            q.append(i);
            answer+=1;
        # 큐에 아무것도 없을때         
        elif len(q) != cacheSize :
            answer +=5;
            q.append(i);
        elif i not in q :
            q.popleft();
            q.append(i);
            answer+=5;
            
            
    return answer
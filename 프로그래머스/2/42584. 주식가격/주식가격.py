from collections import deque

def solution(prices):
    answer = [];
    q = deque(prices);
    
    while q :
        stock = q.popleft();
        idx = 0;
        for i in q :
            idx += 1;
            if i < stock :
                break;
        answer.append(idx);
        
    return answer
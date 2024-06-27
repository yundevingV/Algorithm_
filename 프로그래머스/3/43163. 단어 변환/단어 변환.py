from collections import deque

    
def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append((begin,0))
    # 단어 방문 
    visited = set()
    while q :
        w,idx = q.popleft()
        # 현재 단어랑 target 이랑 같으면 return idx 
        if w == target :
            return idx
        for word in words :
            # 방문하지 않고 한글자만 다르면 q 에 삽입
            if word not in visited and sum([w[i] != word[i] for i in range(len(word))]) == 1 :
                q.append((word,idx+1))
                visited.add(word)
        
    return answer
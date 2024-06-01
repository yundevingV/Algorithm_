from collections import deque

def solution(priorities, location):
    answer = 1
    q = deque(priorities)
    index = location
    while len(q)>1 :
        pop = q.popleft()
        if pop < max(q):
            q.append(pop)
            if index == 0:
                index = len(q) - 1
            else:
                index -= 1
        else:
            if index == 0:
                return answer
            else:
                answer += 1
                index -= 1
    return answer

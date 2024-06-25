from collections import deque

def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees :
        s= '';
        for j in range(len(i)) :
            if i[j] in skill :
                s += i[j];
        if s == skill[:len(s)] :
            answer += 1;
            
    return answer
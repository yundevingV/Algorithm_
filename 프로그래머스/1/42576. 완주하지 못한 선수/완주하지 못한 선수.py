from collections import Counter


def solution(participant, completion):
    answer = '';
    
    c1 = Counter(participant);
    c2 = Counter(completion);
    
    for i in c1 :
        if c1[i] != c2[i] :
            return i;
    return answer
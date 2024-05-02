def solution(s):
    same = 0
    diff = 0
    answer = 0
    sameChar = ''
    
    for i in s:
        if same == 0:
            sameChar = i
        
        if sameChar != i:
            diff += 1
        elif sameChar == i:
            same += 1
        
        if diff == same:
            answer += 1
            same = 0
            diff = 0
            sameChar = ''
        
    if sameChar :
        answer +=1;
        
    return answer
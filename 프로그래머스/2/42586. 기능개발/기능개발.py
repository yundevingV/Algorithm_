import math

def solution(progresses, speeds):
    answer = [];
    
    count = 1;
    a = 100 - progresses[0];
    a = a / speeds[0];
    a = math.ceil(a)
    
    for i in range(1,len(progresses)) :

        b = 100 - progresses[i];
        b = b / speeds[i];
        b = math.ceil(b)

        if a >= b :
            count += 1;
        elif a < b :
            answer.append(count);
            count = 1;
            a = b;
    answer.append(count);
    return answer
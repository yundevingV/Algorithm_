def solution(k, tangerine):
    answer = 0;
    d = {};
    for i in tangerine : 
        if (i in d) :
            d[i] += 1;
        else :
            d[i] = 1;
            
    d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

    for i in d :
        k -= d[i];
        answer+=1;
        if (k <= 0) :
            break;
            
    return answer
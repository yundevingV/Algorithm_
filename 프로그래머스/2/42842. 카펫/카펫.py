def solution(brown, yellow):
    answer = [0,0];
    # 전체면적
    total = brown + yellow;
    
    for w in range(total,1,-1) :
        if (total % w) : continue;
        h = total / w;
        y = (w-2) * (h-2);
        b = total - y;
        
        if y == yellow and b == brown :
            answer[0] = w;
            answer[1] = h;
            break;
    return answer
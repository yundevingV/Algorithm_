def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)

    # 남은사과가 한 박스에 들어가는 사과가 많을때
    
    for i in range(0,len(score),m) :
        if len(score[i:i+m]) == m :
            answer += min(score[i:i+m]) * m
    

    return answer
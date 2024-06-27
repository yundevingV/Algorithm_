def solution(food):
    answer = ''
    
    for i in range(1,len(food)) :
        for j in range(food[i] // 2) :
            answer += str(i)
            
    reversed_str = "".join(reversed(answer))
    answer += '0'
    answer += reversed_str
    return answer
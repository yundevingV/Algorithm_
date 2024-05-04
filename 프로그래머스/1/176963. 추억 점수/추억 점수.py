def solution(name, yearning, photo):
    answer = []
    dict = {}
    for i in range(0,len(name)) :
        dict[name[i]] = yearning[i];

    
    for i in photo :
        score = 0;
        for j in i :
            if j in dict :
                score += dict[j];
        answer.append(score);
        
    return answer;
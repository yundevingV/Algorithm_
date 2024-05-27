def solution(clothes):
    
    d = {}

    for name, kind in clothes:
        if kind in d.keys():
            d[kind] += [name]
        else:
            d[kind] = [name]
    answer = 1;
    
    for i,j in d.items() :
        answer *= (len(j) + 1)
    
    answer -= 1;
    
    return answer
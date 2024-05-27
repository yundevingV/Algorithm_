def solution(s):
    answer = []
    lst = [];
    result = [];
    for i in s.split('},') :
        i = i.replace('{','').replace('}','').split(',');
        lst.append(i);
    
    lst.sort(key=len)
    
    for i in range(len(lst)) :
        for j in range(len(lst[i])) :
            if lst[i][j] not in result : 
                result.append(lst[i][j]);
    result = list(map(int,result))
    return result
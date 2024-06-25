def solution(x, y, n):
    answer = 0
    dp = set()
    dp.add(x)
    
    while dp :
        if y in dp : 
            return answer;
        else : 
            dp_copy = set()
            for i in dp :
                if i + n <= y :
                    dp_copy.add(i+n)
                if i * 2 <= y :
                    dp_copy.add(i*2)
                if i * 3 <= y :
                    dp_copy.add(i*3)
            dp = dp_copy
            answer += 1
        
        
    return -1
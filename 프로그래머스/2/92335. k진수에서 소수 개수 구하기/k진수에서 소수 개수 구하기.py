def solution(n, k):
    answer = 0;
    
    word = '';
    
    while n :
        word = str(n%k) + word;
        n = n // k;
    word = word.split('0');
    
    for i in word :
        prime = True;
        if len(i) == 0:
                    continue;
        if int(i) < 2 :
            continue;
        
        else :
            for j in range(2,int(int(i)**0.5)+1): 
                if int(i)%j==0:
                    prime = False;
                    break;
            if prime : 
                answer+=1;
            
            
        
    return answer
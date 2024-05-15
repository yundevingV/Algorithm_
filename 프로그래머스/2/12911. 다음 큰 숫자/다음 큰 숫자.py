def solution(n):
    answer = 0;
    for i in range(n+1,1000000) :
        
        count1 = bin(n)[2:].count('1');
        count2 = bin(i)[2:].count('1');
        if count1 == count2 :
            return i;
            
        
    
from collections import Counter


def solution(want, number, discount):
    answer = 0;
    dict = {};
    for i in range(len(want)) :
        dict[want[i]] = number[i];
    for i in range(len(discount)-9) : 
        if Counter(discount[i:i+10]) == dict :
            answer +=1;
        
    
    return answer
from collections import Counter

def solution(topping):
    answer = 0;
    dict = Counter(topping);
    set_dict = set();
    for i in topping :
        dict[i] -= 1;
        set_dict.add(i);
        if dict[i] == 0 :
            dict.pop(i);
        if len(dict) == len(set_dict) :
            answer += 1;
    return answer
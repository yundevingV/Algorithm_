def solution(elements):
    answer = 0;
    eSet = set();
    eLen = len(elements);
    elements *=2;
    for i in range(eLen) :
        for j in range(eLen) :
            eSet.add(sum(elements[j:j+i+1]));
        
    return len(eSet)
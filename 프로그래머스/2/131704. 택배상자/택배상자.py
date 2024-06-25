def solution(order):
    s = []
    i = 0
    n = 0 
    while i < len(order) :
        if order[i] > n :
            n += 1
            s.append(n)
        elif s[-1] == order[i] :
            s.pop()
            i += 1
        else :
            return i
        
    return i
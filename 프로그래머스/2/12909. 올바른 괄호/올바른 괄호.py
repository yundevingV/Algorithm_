def solution(s):
    answer = True
    stack = [];
    for i in s :
        if i == '(' :
            stack.append(i);
        elif i == ')' :
            if stack :
                stack.pop();
            else : 
                answer = False;
                break;
    if stack :
        answer = False;
    return answer
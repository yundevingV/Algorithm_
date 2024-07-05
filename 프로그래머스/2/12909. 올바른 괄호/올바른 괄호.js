function solution(s){
    var answer = true;
    let stack = []
    
    for (let i =0 ; i < s.length ; i++){    
        if(s[i] == '('){
            stack.push(s[i])
        }
        else if(s[i] == ')'){
            if(stack[stack.length-1] == '('){
                stack.pop()    
            }
            else { 
                answer = false
                break
            }
        }
        
    }

    if (stack.length > 0) { answer = false}

    return answer;
}
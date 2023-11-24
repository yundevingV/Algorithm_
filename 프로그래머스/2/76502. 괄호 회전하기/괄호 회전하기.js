function solution(s) {
    let answer = 0;

    let stack = [];
    if (s.length % 2 === 1) return 0;

    for(let i = 0; i < s.length ; i++){
        let str = s.slice(i) + s.slice(0,i);
        let count = 1;
        for(j of str){
            if(j ==='[' || j === '{' || j ==='('){
                stack.push(j);
            }
            else {
                let compareWord = stack.pop();
                if(j === ']' && compareWord === '[') {continue;}
                if(j === '}' && compareWord === '{') {continue;}
                if(j === ')' && compareWord === '(') {continue;}
                count = 0;
                console.log(count)

                break;
            }
        }
        
        if(count){answer++;}
        
    }
    
    return answer;
}
function solution(progresses, speeds) {
    var answer = [];
    let i = 1;
    while (progresses.length > 0) {
        
        if (progresses[0] + i * speeds[0] >= 100) {
            progresses.shift();
            speeds.shift();
            answer.push(i);
        }
        else {
            i++;  
        }
    }
    
    let count = 1;
    let day = answer[0];
    let stack = [];

    for(let i=1;i<answer.length;i++) {
        if(answer[i] === day) {
            count++;
        }    
        else {
            stack.push(count);
            count = 1;
            day = answer[i];
        }
    }
    stack.push(count);
    return stack;
}
function solution(priorities, location) {
    var answer = 1;
    
    let queue = priorities;
    let index = location;
    
    while(queue.length) {
        let pop = queue.shift();
        
        // pop가 작으면 다시 큐에 삽입
        if(pop < Math.max(...queue)) {
            queue.push(pop);
            if(index === 0) {
                index = queue.length - 1; 
            }
            else {
                index -= 1;
            }
        }
        // pop가 크거나 같으면 실행
        else {
            if(index === 0){
                return answer;
            }
            else {
                answer += 1;
                index -= 1;
            }
        }
    }

    return answer;
}
function solution(prices) {
    var answer = [];
    
    for(let i=0;i<prices.length;i++) {
        let count = 0;
        for(let j=i+1;j<prices.length;j++) {
            if(prices[i] > prices[j]) {
                count += 1;
                break;
            }
            else count += 1;
        }
        answer.push(count);
    }
    return answer;
}
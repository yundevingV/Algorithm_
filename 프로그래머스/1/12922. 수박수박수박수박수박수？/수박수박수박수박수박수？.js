function solution(n) {
    var answer = '';
    for(let i = 0; i < n ; i++) {
        if( (i+1) % 2) {
            answer += '수'
        }
        
        else {
            answer +='박'
        }
    }
    return answer;
}
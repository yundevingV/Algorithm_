function solution(s) {
    var answer = [];
    
    for(let i=0;i<s.length;i++) {
        let list = s.slice(0,i);
        let index = list.lastIndexOf(s[i]);
        if (index === -1) {
            answer.push(index);
        }
        else {
            answer.push(i - index);
        }
    }

    return answer;
}
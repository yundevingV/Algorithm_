function solution(s, n) {
    var answer = '';
    
    let list = [];
    
    for(let i=0;i<s.length;i++) {
        let askiiNum = s[i].charCodeAt();
        if (askiiNum === 32) {
            list.push(32);
            continue;
        }
        
        if (askiiNum >= 65 && askiiNum <= 90) {
            if (askiiNum + n > 90) {
                
                askiiNum = askiiNum + n - 26;
                list.push(askiiNum);
            }
            else {
                list.push(askiiNum + n);
            }
        }
        
        else if (askiiNum >= 97 && askiiNum <= 122) {
            if (askiiNum + n > 122) {
                askiiNum = askiiNum + n - 26;
                list.push(askiiNum);
            }
            else {
                list.push(askiiNum + n);
            }
        }
    }
    
    // 아스키코드 -> 문자 변환
    for(let i=0;i<list.length;i++) {
        
        answer += String.fromCharCode(list[i])
    }
    
    return answer;
}
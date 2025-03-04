function solution(babbling) {
    var answer = 0;
    let ong = ['aya', 'ye', 'woo', 'ma'];
    
    for (let i = 0; i < babbling.length; i++) {
        let str = babbling[i];
        
        for (let j = 0; j < ong.length; j++) {
            if(str.includes(ong[j])){
                str = str.replace(ong[j], 'X');
                }
        }
        str = str.replace(/X/gi, '');
        if(str === '') answer += 1;
    }
    
    return answer;
}

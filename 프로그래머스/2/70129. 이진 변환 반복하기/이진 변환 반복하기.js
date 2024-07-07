function solution(s) {
    var answer = [];
    let a = 0
    let b = 0
    while (s != '1') {
        a += s.length - s.replaceAll('0','').length
        s = s.replaceAll('0','') 
        s = s.length.toString(2)
        b+=1
    }
    answer.push(b)
    answer.push(a)
    return answer;
}
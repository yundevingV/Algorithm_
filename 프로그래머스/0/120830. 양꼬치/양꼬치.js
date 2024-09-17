function solution(n, k) {
    var answer = 0;
    k -= Math.floor(n / 10);
    
    answer += n * 12000
    answer += k * 2000
    return answer;
}
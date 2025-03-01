function solution(a, b, n) {
    let answer = 0;

    while (n >= a) { 
        let exchangedBottles = Math.floor(n / a) * b;
        answer += exchangedBottles; 
        n = exchangedBottles + (n % a); 
    }

    return answer; 
}
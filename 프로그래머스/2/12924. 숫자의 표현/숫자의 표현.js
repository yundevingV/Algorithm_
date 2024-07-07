function solution(n) {
    var answer = 0;
    let sum = 0;
    let mod_n = n/2+1 
    
    for(let i=1 ; i<mod_n ; i++){
        sum = 0;
        for(let j=i ; j<mod_n ; j++){
            sum +=j
            if(sum > n){
                break
            }
            else if(sum == n) {
                answer +=1
                break
            }
    }    
    }
    return n == 1 ? 1 : ++answer;
}
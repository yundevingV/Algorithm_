

function solution(q1, q2) {
    var answer = 0;

    let q = [...q1,...q2];
    let sum1 = q1.reduce((prev, cur) => prev + cur, 0);
    let sum2 = q2.reduce((prev, cur) => prev + cur, 0);
    let middle = (sum1 + sum2) / 2;

    
    let p1 = 0;
    let p2 = q1.length;
    
    for(let i = 0; i < q.length * 2 ; i++){

        if(sum1 === middle){return i;}
        
        if(sum1 > middle) {
            sum1 -= q[p1 % q.length]
            p1 +=1;
        }
        else {
            sum1 += q[p2 % q.length]
            p2+=1;
        }
    }
    return -1;

}
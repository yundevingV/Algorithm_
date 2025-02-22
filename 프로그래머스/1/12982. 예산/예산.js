function solution(d, budget) {
    var answer = 0;
    const len = d.length;
    
    d.sort((a,b) => a-b);
    
   for(let i=0;i<len;i++){
       if(budget < d[i]) break;
       
       budget -= d[i];
       answer += 1;
   }
    
    return answer;
}
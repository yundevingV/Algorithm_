// 1. sort로 도전!

function solution(k, score) {
    var answer = [];
    let scoreList = [];
    let len = score.length;
    
    for(let i=0;i<len;i++){
        
        if(scoreList.length === k){ 
            if(scoreList[0] < score[i]) {
                scoreList.shift();    
                scoreList.push(score[i]);
            }
        } else {
            scoreList.push(score[i]);
        }
        
        scoreList.sort((a, b) => {
            return a - b; 
        });
        
        answer.push(scoreList[0]);
    }
    return answer;
}
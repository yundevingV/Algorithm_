function solution(answers) {
    let answer=[]
    var score = [0,0,0];
    let one = [1,2,3,4,5]
    let two = [2,1,2,3,2,4,2,5]
    let three = [3,3,1,1,2,2,4,4,5,5]
    
    let len = answers.length
    for(let i = 0; i < len; i++){
        if(answers[i] == one[i%one.length]){
            score[0] += 1
        }
        if(answers[i] == two[i%two.length]){
            score[1] += 1
        }
        if(answers[i] == three[i%three.length]){
            score[2] += 1
        }
    }
    for(let i = 0;i<score.length ; i++){
        if(Math.max(...score) == score[i]){
            answer.push(i+1)
        }
    }
    return answer;
}
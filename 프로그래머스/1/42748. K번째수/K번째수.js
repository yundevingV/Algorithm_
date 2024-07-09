function solution(array, commands) {
    var answer = [];
    for(let i = 0 ;i<commands.length;i++){
        let s = commands[i][0]-1
        let e = commands[i][1]
        let idx = commands[i][2]-1
        arr = array.slice(s,e)
        arr.sort((a,b) => a - b)
        answer.push(arr[idx])
    }
    return answer;
}
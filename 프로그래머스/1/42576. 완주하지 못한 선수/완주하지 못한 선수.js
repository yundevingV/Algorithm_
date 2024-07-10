function solution(participant, completion) {
    var answer = '';
    let map = new Map()
    for(let i =0;i<participant.length;i++){
        let p = participant[i]
        let c = completion[i]
        // 참가자 집어넣기
        map.set(p, (map.get(p) || 0) + 1 )
        // 도착자 빼기
        map.set(c, (map.get(c) || 0) - 1 )
    }
    map.forEach((v,i) =>{
        if(v > 0){
            answer = i
        }
    })
    
    return answer;
}
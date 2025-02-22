// 1. video_len 을 초로 변환
// 2. 오프닝 구간인지 체크 -> 오프닝이면 끝시간으로 이동
// 3. command 명령을 따라감 
// 3-1. 넥스트면 끝시간, 프리브면 첫시간 

function mmssToSeconds(pos){
    const [m,s] = pos.split(':');
    
    return Number(m) * 60 + Number(s);
}

function secondsToMmss(seconds){
    const m = String(Math.floor(seconds / 60));
    const s = String(seconds % 60);
    console.log(m,s)
    return m.padStart(2,"0") + ':' + s.padStart(2,"0")
}

function solution(video_len, pos, op_start, op_end, commands) {
    var answer = '';
    
    const len = commands.length;
    
    const op_start_seconds = mmssToSeconds(op_start);
    const op_end_seconds = mmssToSeconds(op_end);
    const video_len_seconds = mmssToSeconds(video_len);
    
    let pos_seconds = mmssToSeconds(pos);
    
    if(op_start_seconds <= pos_seconds && pos_seconds <= op_end_seconds){
        pos_seconds = op_end_seconds;
    }
    
    for(let i=0;i<len;i++){
       
        if(commands[i] === 'next'){
            if(pos_seconds + 10 > video_len_seconds){
                pos_seconds = video_len_seconds;
            } else {
                pos_seconds+=10;
            }
        }
        if(commands[i] === 'prev'){
            if(pos_seconds - 10 < 0){
                pos_seconds = 0;
            } else {
                pos_seconds-=10;
            }
        }
        if(op_start_seconds <= pos_seconds && pos_seconds <= op_end_seconds){
            pos_seconds = op_end_seconds;
        }
    }
     
    return secondsToMmss(pos_seconds);
}
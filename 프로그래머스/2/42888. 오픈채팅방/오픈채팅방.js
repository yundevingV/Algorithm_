function solution(record) {
    var answer = [];
    const idMap = new Map();
    
    record.forEach((record)=> {
        const [action,uid,name] = record.split(' ');    
        if(action === 'Enter') {
            if(idMap.has(uid)) {
                idMap.delete(uid);
                idMap.set(uid,name);
                answer.push(uid + ' ' + action);
            } else {
                idMap.set(uid,name);
                answer.push(uid + ' ' + action);
            }
        }
        else if(action === 'Leave') {
            answer.push(uid + ' ' + action);
        }
        else if(action === 'Change') {
            if(idMap.has(uid)) {
                idMap.delete(uid);
                idMap.set(uid,name);
            } 
        }
    });
    
    let result = [];
    answer.forEach((item) => {
        const [id,action] = item.split(' ');
        if(action === 'Enter') {
            result.push(`${idMap.get(id)}님이 들어왔습니다.`);
        } 
        else if(action === 'Leave') {
            result.push(`${idMap.get(id)}님이 나갔습니다.`);
        }
        
    })
    
    return result;
}
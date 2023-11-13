function lower(new_id){
    new_id = new_id.toLowerCase();
    return new_id;
}

function d(new_id){
    new_id = new_id.replace(/[^a-z0-9-_.]/g, '');
    return new_id;
}

function dot(new_id){
    new_id = new_id.replace(/\.{2,}/g,'.');
    return new_id;
}
function dot2(new_id){
    new_id = new_id.replace(/^\.|\.$/g, '');
    return new_id;

}
function empty(new_id){
    
    if(new_id.length !== 0 ){
        return new_id;

    } else {
        new_id = 'a';
        return new_id;
    }
}

function long(new_id){

    if(new_id.length >= 16){
        new_id = new_id.substring(0,15);
        if(new_id[new_id.length-1] === '.'){
            console.log('.')
            new_id = new_id.replace(/\.$/g,'');
            return new_id;
        }
        else {
            return new_id;
        }
    }
    else {
        return new_id;
    }
}

function fill(new_id) {
    if (new_id.length <= 2) {
        while (new_id.length !== 3) {
            new_id = new_id.concat(new_id[new_id.length - 1]);
        }
    }
    return new_id;
}
function solution(new_id) {
    // 대문자 -> 소문자
    new_id = lower(new_id);

    //  알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    new_id = d(new_id);
    //  ..2개 이상 . 치환
    new_id = dot(new_id);
    //  앞뒤 . 제거
    new_id = dot2(new_id);
    //  빈문자열일때 a 대입
    new_id = empty(new_id);

    new_id = long(new_id);
    new_id = fill(new_id);
    console.log(new_id);
    
    var answer = new_id;
    return answer;
}


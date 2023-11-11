// 범위지정

function solution(s, skip, index) {

    // skip
    let skipLst = [];
    for (i in skip){
        skipLst.push(skip[i].charCodeAt());
    }
    // 아스키코드 저장할 배열
    let answerLst = [];
    let jump = 0;

    for(i in s){
        let word = s[i].charCodeAt();
        let jump = 0;
        for(j=0;j<index;j++){
            word+=1 
            if(word > 122){word-=26}

            if(skipLst.includes(word)){ j-=1 } 
            
        }   
        answerLst.push(word);
    }


    let resultString = answerLst.map(code => String.fromCharCode(code)).join('');

    var answer = resultString;
    return answer;
}
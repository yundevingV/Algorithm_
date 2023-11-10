function solution(survey, choices) {
    var answer = '';

    let dict = {"R" : 0 , "T" : 0 , "C" : 0 , "F" : 0 , 
                "J" : 0 , "M" : 0 , "A" : 0 , "N" : 0};
    
    let alpha = ["RT","CF","JM","AN"];
    console.log(survey)
    for(i in survey){
        console.log(survey[i], (choices[i]))
        // 전자를 선택
        
        if(1 <= choices[i] && choices[i]  <= 3 ){ 
            
            if (choices[i] == 1) {dict[survey[i][0]] += 3}
            else if (choices[i] == 2 ){dict[survey[i][0]] += 2}
            else {dict[survey[i][0]] += 1}
        } 
        // 후자를 선택         
        else if (5 <= choices[i] && choices[i] <= 7){
            dict[survey[i][1]] += choices[i] - 4

        } 
        
        console.log(dict)
    }
    
    for(i in alpha){
        
        if(dict[alpha[i][0]] < dict[alpha[i][1]]) 
           {
                answer+=([alpha[i][1]]); 
           }
        else
           {
                answer+=([alpha[i][0]]);
           }
 
    }
    
    
    return answer;
}
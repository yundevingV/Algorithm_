// 투포인터
// sum이 k보다 크면 s+1 sum -= sequence[s]
// sum이 k보다 작으면 e-1 sum += sequence[e]

function solution(sequence, k) {
    var answer = [];
    let start = 0;
    let end = 0;
    let len = sequence.length;
    let sum = 0;

    while (start <= len && end <= len) {
        if(sum < k) {
            sum += sequence[end];
            end += 1;
        } 
        else if(sum > k) {
            sum -= sequence[start];
            start += 1;
        }
        else if (sum === k){
            answer.push([start, end - 1, end - 1 - start]);
            sum -= sequence[start];
            start += 1;
        }
    }
    
    answer.sort((a, b) => {
        if (a[2] === b[2]) {
            return a[0] - b[0];
        }
        return a[2] - b[2];
    });
    
    answer[0].pop();
    
    return answer[0];
}
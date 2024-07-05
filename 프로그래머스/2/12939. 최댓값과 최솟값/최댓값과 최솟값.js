function solution(s) {
    var answer = '';
    const arr = s.split(' ')
    console.log(arr[0])
    let min_num = Math.min(...arr)
    let max_num = Math.max(...arr)
    answer = min_num + ' ' + max_num 
    return answer;
}
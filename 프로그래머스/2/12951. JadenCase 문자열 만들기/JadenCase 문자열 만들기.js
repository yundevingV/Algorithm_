function solution(s) {
    var answer = '';
    const arr = s.split(' ').map(x => x.substr(0,1).toUpperCase() + x.substr(1).toLowerCase())
    return arr.join(' ');
}
function solution(nums) {
    var answer = 0;
    const set = new Set(nums)
    const uniqueArr = [...set]
    
    if (uniqueArr.length > nums.length / 2){
        return nums.length / 2
    }
    else {
        return uniqueArr.length
    }
    return answer;
}
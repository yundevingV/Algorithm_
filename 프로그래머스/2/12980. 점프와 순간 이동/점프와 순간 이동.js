function solution(n)
{
    var ans = 0;
    while (true) {
        if(n == 0){
            break
        }
        // 홀수면
        if(n % 2 == 1) {
            ans +=1
            n -= 1
        }
        // 짝수면
        else if(n % 2 == 0){
            n = n/2
        }
    }
    

    return ans;
}
function solution(n, works) {
    if(works.reduce((a,b) => a+b) <= n) return 0;

    let len = works.length;
    let sortedWorks = works.sort((a,b) => a - b);

    while(n) {
        let max = sortedWorks[len - 1];
        for(let i=len-1;i>=0;i--){
            if(max <= sortedWorks[i]){
                sortedWorks[i]--;
                n--;
            }
            if(!n) break
        }
    }
    return sortedWorks.reduce((acc,cur) => acc + Math.pow(cur, 2),0);
}

function solution(m, n, b) {
    var answer = 0;
    let board = b.map((row) => row.split(''));

    while (true) {
        let mark  = Array.from({ length: m }, () => new Array(n).fill(0));
        let hasMarked = false;
        
        for(let i=0;i<m-1;i++) {
            for(let j=0;j<n-1;j++) {

                const value = board[i][j];
                if(!value) continue;

                const isRight = value === board[i+1][j];
                const isBottom = value === board[i][j+1];
                const isRightBottom = value === board[i+1][j+1];

                if(isRight && isBottom && isRightBottom) {
                    hasMarked = true;
                    mark[i][j] = 1;
                    mark[i+1][j] = 1;
                    mark[i][j+1] = 1;
                    mark[i+1][j+1] = 1;
                }
            }
        }
        
        if(!hasMarked) break;
        
        // marking
        for(let i=0;i<mark.length;i++) {
            for(let j=0;j<mark[0].length;j++) {
                if(mark[i][j] === 1) {
                    board[i][j] = 0;
                    answer+=1;
                }
            }
        }
        
        //moving
        for(let j=0;j<n;j++) {
            let floor = m-1;
            for(let i=m-1;i>=0;i--) {
                if(board[i][j]) {
                    let temp = board[i][j];
                    board[i][j] = 0;
                    board[floor][j] = temp;
                    floor--;
                }
            }
        }
    }
    
    return answer;
}
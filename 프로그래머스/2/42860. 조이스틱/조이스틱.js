function solution(name) {
    const nameList = [...name];
    const n = nameList.length;

    const upCountStick = () => {
        return nameList.reduce((acc, cur) => {
            const aAskii = 'A'.charCodeAt();
            const zAskii = 'Z'.charCodeAt();
            
            const upStick = cur.charCodeAt() - aAskii;
            const downStick = zAskii - cur.charCodeAt() + 1;
            
            const result = acc + Math.min(upStick, downStick);
            return result;
        }, 0);
    }
        
    const moveCountStick = () => {
        let minMove = n - 1; 

        for (let i = 0; i < n; i++) {
            let nextIndex = i + 1;
            
            while (nextIndex < n && nameList[nextIndex] === 'A') {
                nextIndex++;
            }
            
            minMove = Math.min(
                minMove,
                i * 2 + (n - nextIndex),
                i + (n - nextIndex) * 2
            );
        }
        return minMove;
    }
    
    return upCountStick() + moveCountStick();
}
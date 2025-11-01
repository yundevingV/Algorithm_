const convertMinutes = (time) => {
    const timeSplit = time.split(':');
    
    const hours = Number(timeSplit[0]);
    const minutes = Number(timeSplit[1]);
    
    return hours * 60 + minutes;
}

function solution(fees, records) {
    const [baseTime, baseFee, unitTime, unitFee] = fees;
    
    let carsMap = new Map(); 
    let timeMap = new Map(); 
    
    records.forEach((record) => {
        const recordSplit = record.split(' ');
        let time = recordSplit[0];
        const convertedTime = convertMinutes(time); 
        const carNumber = recordSplit[1];
        const status = recordSplit[2];
        
        if (status === 'IN') {
            carsMap.set(carNumber, convertedTime);
        }
        else { 
            let inTime = carsMap.get(carNumber);
            let outTime = convertedTime;
            let parkingTime = outTime - inTime; 
            
            let prevTime = timeMap.get(carNumber) || 0;
            timeMap.set(carNumber, prevTime + parkingTime);
            
            carsMap.delete(carNumber);
        }
    });

    const finalOutTime = convertMinutes("23:59"); 
    
    carsMap.forEach((inTime, carNum) => {
        let parkingTime = finalOutTime - inTime;
        let prevTime = timeMap.get(carNum) || 0;
        timeMap.set(carNum, prevTime + parkingTime);
    });

    const sortedTimeArr = [...timeMap].sort((a, b) => a[0].localeCompare(b[0]));
    
    const answer = sortedTimeArr.map(([carNum, totalTime]) => {
        if (totalTime <= baseTime) {
            return baseFee;
        }
        return baseFee + Math.ceil((totalTime - baseTime) / unitTime) * unitFee;
    });

    return answer;
}
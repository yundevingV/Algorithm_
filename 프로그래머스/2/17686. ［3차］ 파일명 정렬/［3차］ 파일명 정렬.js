const classifyFileName = (file) => {
    const regex = /^([^0-9]+)([0-9]+)(.*)$/;
    const match = file.match(regex);
    return { head: match[1], number: match[2].slice(0,5), tail: match[3] };
}

function solution(files) {
    files.sort((a, b) => {
        
        const fileA = classifyFileName(a);
        const fileB = classifyFileName(b);
        const headCompare = fileA.head.localeCompare(fileB.head, 'en', { sensitivity: 'base' });
        
        const formattingNum = (num) => {
            let index = 0;
            for(let i=0;i<num.length;i++) {
                if (num[i] !== "0") {                    
                  index = i;
                  return num.slice(i,num.length);   
                }
                else return num;
            }
        }
        const numCompare = parseInt(formattingNum(fileA.number, 10)) - parseInt(formattingNum(fileB.number, 10));

        return headCompare || numCompare;
    });

    return files;
}
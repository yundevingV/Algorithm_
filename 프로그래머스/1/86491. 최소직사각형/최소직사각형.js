function solution(sizes) {
    let w = 0;
    let h = 0;

    for(let i = 0; i < sizes.length; i++){
        let maxSize = Math.max(sizes[i][0], sizes[i][1]);
        let minSize = Math.min(sizes[i][0], sizes[i][1]);
        
        w = Math.max(w, maxSize);
        h = Math.max(h, minSize);
    }

    return w * h;
}

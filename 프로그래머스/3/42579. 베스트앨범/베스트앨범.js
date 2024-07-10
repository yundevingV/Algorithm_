function solution(genres, plays) {
    var answer = [];
    let total_map = new Map();

    // 각 장르별 총 재생 수 계산
    for(let i = 0; i < genres.length; i++) {
        let key = genres[i];
        let value = plays[i];
        
        if(!total_map.has(key)) {
            total_map.set(key, value);
        } else {
            total_map.set(key, total_map.get(key) + value);
        }
    }
    
    // 장르별 노래 정보 저장
    let song_map = genres.map((genre, index) => ({
        genre: genre,
        index: index,
        count: plays[index]
    }));
    
    // 장르별 총 재생 수를 기준으로 내림차순 정렬
    let sortedByValue = new Map([...total_map.entries()].sort((a, b) => b[1] - a[1]));
    
    // 정렬된 장르별로 노래 인덱스를 가져와 answer에 추가
    sortedByValue.forEach((totalPlays, genre) => {
        // 해당 장르의 노래들을 재생 수와 인덱스로 정렬
        let songsInGenre = song_map.filter(song => song.genre === genre);
        songsInGenre.sort((a, b) => b.count - a.count || a.index - b.index);
        
        // 상위 2곡의 인덱스를 answer에 추가
        for(let i = 0; i < Math.min(2, songsInGenre.length); i++) {
            answer.push(songsInGenre[i].index);
        }
    });

    return answer;
}


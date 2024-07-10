function solution(word) {
    var answer = 0;
    let words = ['A', 'E', 'I', 'O', 'U'];
    let found = false;

    const dfs = (currentWord) => {
        if (currentWord.length > 0) {
            answer++;
        }
        
        if (currentWord === word) {
            found = true;
            return;
        }

        if (currentWord.length >= 5) {
            return;
        }

        for (let i = 0; i < words.length; i++) {
            if (!found) {
                dfs(currentWord + words[i]);
            }
        }
    }

    dfs('');
    return answer;
}


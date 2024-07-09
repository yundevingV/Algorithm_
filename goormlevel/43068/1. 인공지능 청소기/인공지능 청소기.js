

const readline = require('readline');

(async () => {
  let rl = readline.createInterface({ input: process.stdin });
  let N = null;
  let count = 0;
  const data = [];

  for await (const line of rl) {
    if (!N) {
      N = +line;
    } else {
      
      
      data.push(line.split(' ').map((el) => Number(el)));
      
      count += 1;
    }
    if (N === count) {
      rl.close();
			
    }
  }
	
	for(let i=0; i< N ; i++){
		let s = Math.abs(data[i][1]) + Math.abs(data[i][0])
		let t = data[i][2]	
		if( (s <= t) && (( s - t) % 2 === 0 ))  {
			console.log("YES")
		} else {
			console.log("NO")
		}
	}
  process.exit();
})();
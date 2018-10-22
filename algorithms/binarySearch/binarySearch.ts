function search(array: number[], targetValue: number): number {
	let min = 0;
	let max = array.length - 1;
    let guess;
    while(max >= min) {
        guess = Math.floor((max + min)/2);
        if (array[guess] === targetValue) {
            return guess;
        }
        if (array[guess] < targetValue) {
            min = guess + 1;
        }
        if (array[guess] > targetValue) {
            max = guess - 1;
        }
    }
	return -1;
}

const primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71];

console.log(search(primes, 67) === 18);
console.log(search(primes, 73) === -1);

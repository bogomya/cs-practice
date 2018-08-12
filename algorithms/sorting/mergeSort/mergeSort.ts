function merge(a1: number[], a2: number[]): number[] {
	if (!a1.length) {
		return a2;
    }
	if (!a2.length) {
		return a1;
    }
	if (a1[0] > a2[0]) {
		return [a2[0], ...merge(a1, a2.slice(1))];
	} else {
    	return [a1[0], ...merge(a2, a1.slice(1))];
	}
}

function mergeSort(arr: number[]): number[] {
    if (arr.length === 1) {
        return arr;
    }
    const index = Math.floor(arr.length / 2);
    return merge(mergeSort(arr.slice(0,index)), mergeSort(arr.slice(index)));
}

console.log(mergeSort([10, 3, 9, 15, 2, 3, 1]).toString() === [1, 2, 3, 3, 9, 10, 15].toString());

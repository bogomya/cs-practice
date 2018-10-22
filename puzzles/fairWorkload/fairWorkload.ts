function getMostWork(folders: number[], workers: number) {
    let min = Math.max(...folders);
    let max = folders.reduce((sum, folder) => sum + folder, 0);
    let final = 0;

    if (workers  == 1) {
        return max;
    }

    while (max > min) {
        const possibleLoad = (max + min)/2;
        let currentGroupLoad = 0;
        let requiredWorkers = 1;
        let result = 0;
        for (let i=0; i < folders.length; i++) {
            if (currentGroupLoad + folders[i] <= possibleLoad) {
                currentGroupLoad += folders[i];
            } else {
                requiredWorkers++;
                currentGroupLoad = folders[i];
            }
            result = Math.max(currentGroupLoad, result);
        }
        if (requiredWorkers <= workers) {
            max = possibleLoad;
            final = result;
        } else {
            min = possibleLoad + 1;
        }

    }
    return final;
}


console.log(getMostWork([10, 20, 30, 40, 50, 60, 70, 80, 90], 3) === 170);
console.log(getMostWork([10, 20, 30, 40, 50, 60, 70, 80, 90], 5) === 110);
console.log(getMostWork([568, 712, 412, 231, 241, 393, 865, 287, 128, 457, 238, 98, 980, 23, 782], 4) === 1785);
console.log(getMostWork([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1000], 2) === 1000);
console.log(getMostWork([50, 50, 50, 50, 50, 50, 50], 2) === 200);
console.log(getMostWork([1, 1, 1, 1, 100], 5) === 100);
console.log(getMostWork([950, 650, 250, 250, 350, 100, 650, 150, 150, 700], 6) === 950);
console.log(getMostWork([1, 1], 1) === 2);
console.log(getMostWork([3, 7, 5], 2) === 10);


// [ba, bc, aa, ac, cb] и ordering = [b, a, c]

function checkOrder(strings: string[], priority: string[]) {
    const priorityMap: any = priority.reduce((map, l, i) => {
        return { ...map, [l]: priority.length - i}
    }, {});
    for (let i=0; i < strings.length-1; i++) {
            const item = strings[i];
            const nextItem = strings[i+1];
            for (let j=0; j<item.length; j++) {
                const letterA = item[j];
                const letterB = nextItem[j];
                if (priorityMap[letterB] > priorityMap[letterA]) {
                    return false
                }
                if (priorityMap[letterB] < priorityMap[letterA]) {
                    break
                }
            }
    }
    return true;
}

console.log(checkOrder(["ba", "bc", "aa", "ac", "cb"], ["b", "a", "c"]) === true);
console.log(checkOrder(["aa", "bc", "aa", "ac", "cb"], ["b", "a", "c"]) === false);

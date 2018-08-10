function fib(n: number) {
    let [a, b] = [0, 1];
    if (n === 0) {
        return a;
    }
    if (n === 1) {
        return b;
    }
    for (let i = 2; i <= n; i++) {
        [a, b] = [b, a+b];
    }
    return b;
}

console.log(fib(5) === 5);

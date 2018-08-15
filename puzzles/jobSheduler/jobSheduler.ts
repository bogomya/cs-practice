function scheduleJob(fn: (...args: any[]) => any, n: number) {
    const timeoutId = setTimeout(fn, n);
    return () => clearTimeout(timeoutId);
}

console.log("Before");
scheduleJob(() => console.log("Delayed"), 100);
console.log("After");

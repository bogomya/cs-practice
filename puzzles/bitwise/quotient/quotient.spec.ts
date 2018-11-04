function quotient(x: number, y: number) {
    let res = 0;
    let power = 16;
    let yPowered = (y << power);

    while (x >= y) {
        while (yPowered > x) {
            yPowered >>= 1;
            power -= 1;
        }
        x = x - yPowered;
        res += (1 << power);
    }

    return res;
}

describe("sum", () => {
    it("should return quotient of x / y", () => {
        expect(quotient(10, 1)).toEqual(10);
        expect(quotient(10, 3)).toEqual(3);
        expect(quotient(999, 100)).toEqual(9);
        expect(quotient(1000, 100)).toEqual(10);
    });
});

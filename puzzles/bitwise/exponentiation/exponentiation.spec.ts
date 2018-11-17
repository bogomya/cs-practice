function power(x: number, y: number) {
    let res = 1;
    let power = y;
    if (y < 0) {
        x = 1/x;
        power *= -1;
    }
    while (power) {
        if (power & 1) {
            res *= x;
        }
        x *= x;
        power >>= 1;
    }
    return res;
}

describe("power", () => {
    it("should should return correct parity", () => {
        expect(power(5, 3)).toEqual(125);
        expect(power(7, 1)).toEqual(7);
        expect(power(3, 0)).toEqual(1);
        expect(power(2, -3)).toEqual(0.125);
    });
});

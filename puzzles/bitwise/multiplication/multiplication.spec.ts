function sum(x: number, y: number) {
    let carry = 0;
    let mask = 1;
    let tempX = x;
    let tempY = y;
    let sum = 0;

    while(tempX | tempY) {
        const xk = x & mask;
        const yk = y & mask;

        sum |= xk ^ yk ^ carry;
        carry = ((xk & yk) | (xk & carry) | (yk & carry)) << 1;

        mask <<= 1;
        tempX >>= 1;
        tempY >>= 1;
    }

    return sum | carry;
}

function multiply(x: number, y: number) {
    let res = 0;
    while(x) {
        if (x & 1) {
            res = sum(res, y);
        }
        x >>= 1;
        y <<= 1;
    }
    return res;
}

describe("sum", () => {
    it("should return sum of x and y", () => {
        expect(sum(parseInt("101101", 2), parseInt("100111", 2))).toEqual(parseInt("1010100", 2));
        expect(sum(232, 49)).toEqual(281);
    });

    it("should multiply x and y", () => {
        expect(multiply(parseInt("00001101", 2), parseInt("00001001", 2))).toEqual(parseInt("01110101", 2));
        expect(multiply(33, 4)).toEqual(132);
    })
});

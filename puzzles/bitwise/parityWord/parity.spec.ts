function simpleParity(value: number) {
    let parity = 0;
    while(value) {
        parity ^= value & 1;
        value >>= 1;
    }
    return parity;
}

function erasedFirstSetBitParity(value: number) {
    let parity = 0;
    while(value) {
        parity ^= 1;
        value = value & (value -1); // clear first from the right set (=1) bit
    }
    return parity;
}

describe("parity", () => {
    it("simpleParity should return correct parity", () => {
        expect(simpleParity(5)).toEqual(0);// 00000101
        expect(simpleParity(7)).toEqual(1);// 00000111
    });

    it("erasedFirstSetBitParity should return correct parity", () => {
        expect(erasedFirstSetBitParity(33)).toEqual(0);// 00100001
        expect(erasedFirstSetBitParity(32)).toEqual(1);// 00100000
    });
});

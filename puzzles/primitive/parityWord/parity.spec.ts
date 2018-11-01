function simpleParity(value: number) {
    let parity = 0;
    while(value) {
        parity ^= value & 1;
        value >>= 1;
    }
    return parity;
}

describe("simpleParity", () => {
    it("should return correct parity", () => {
        expect(simpleParity(5)).toEqual(0);// 00000101
        expect(simpleParity(7)).toEqual(1);// 00000111
    });
});

function swapBits(value: number, i: number, j: number) {
    if ((value & (1 << i)) !== (value & (1 << j))) {
        const mask = (1 << i) | (1 << j);
        return value ^ mask;
    }
    return value;
}

describe("swapBits", () => {
    it("should swap bits i and j", () => {
        expect(swapBits(parseInt("01001001", 2), 1, 6)).toEqual(parseInt("00001011", 2));
    });

    it("should return the same number for the same bits i and j", () => {
        expect(swapBits(parseInt("01001001", 2), 1, 2)).toEqual(parseInt("01001001", 2));
    })
});

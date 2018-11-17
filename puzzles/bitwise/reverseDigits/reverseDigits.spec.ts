function reverseDigit(n: number) {
    let rest = n;
    let result = 0;
    while(rest) {
        result = result * 10 + rest % 10;
        rest = Math.floor(rest / 10);
    }
    return result;
}


describe("reverseDigit", () => {
    it("should return reversed number", () => {
        expect(reverseDigit(146)).toEqual(641);
        expect(reverseDigit(7)).toEqual(7);
        expect(reverseDigit(1460)).toEqual(641);
    });
});

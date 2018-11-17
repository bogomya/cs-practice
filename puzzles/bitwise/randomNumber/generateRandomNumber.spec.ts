function generateRandomNumber(from: number, to: number) {
    const difference = to - from;
    let number;
    while (true) {
        number = 0;
        for (let i = 0; (1 << i) <= difference; i++) {
            number = (number << 1) | Math.round(Math.random())
        }
        if (number <= difference) {
            break;
        }
    }
    return from + number;
}

describe("generateRandomNumber", () => {
    it("should render number between from and to", () => {
        const from = 9;
        const to = 99999;
        expect(generateRandomNumber(from, to)).toBeGreaterThanOrEqual(from);
        expect(generateRandomNumber(from, to)).toBeLessThanOrEqual(to);
    });

    it("should return number based on math.random", () => {
        const { random: originalRandom } = global.Math;
        const from = 9;
        const to = 99999;
        global.Math.random = () => 0;
        expect(generateRandomNumber(from, to)).toEqual(from);
        global.Math.random = originalRandom;
    });
});

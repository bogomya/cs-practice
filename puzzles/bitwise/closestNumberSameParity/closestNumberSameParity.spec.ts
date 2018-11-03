/*
The count of ones in binary representation of integer number is called the weight of that number.
The following algorithm finds the closest integer with the same weight.
For example, for 123 (0111 1011)₂, the closest integer number is 125 (0111 1101)₂.
*/

// O(n) complexity
function simpleClosestNumberSameParity(n: number) {
    const binaryLength = 64;
    for (let i=0; i < binaryLength; i++) {
        if (((n >> i) & 1) !== ((n >> i+1) & 1)) {
            return n ^ (1 << i) ^ (1 << i+1);
        }
    }
    return undefined;
}

// O(1) complexity
function closestNumberSameParity(n: number) {
    // validation for 0 and max int
    if (!n || n == Number.MAX_SAFE_INTEGER) {
        return undefined
    }
    const firstSetBit = n & ~(n-1);
    const firstNotSetBit = ~n & (n+1);
    if (firstNotSetBit > firstSetBit) {
        return n ^ firstNotSetBit ^ (firstNotSetBit >> 1);
    } else{
        return n ^ firstSetBit ^ (firstSetBit >> 1);
    }
}

describe("simpleClosestNumberSameParity", () => {
    it("should return correct parity value", () => {
        expect(simpleClosestNumberSameParity(parseInt("01111011", 2))).toEqual(parseInt("01111101", 2));
        expect(simpleClosestNumberSameParity(parseInt("11101100", 2))).toEqual(parseInt("11101010", 2));
        expect(simpleClosestNumberSameParity(parseInt("11101011", 2))).toEqual(parseInt("11101101", 2));
    });
});

describe("closestNumberSameParity", () => {
    it("should return correct parity value", () => {
        expect(closestNumberSameParity(parseInt("01111011", 2))).toEqual(parseInt("01111101", 2));
        expect(closestNumberSameParity(parseInt("11101100", 2))).toEqual(parseInt("11101010", 2));
        expect(closestNumberSameParity(parseInt("11101011", 2))).toEqual(parseInt("11101101", 2));
    });
});

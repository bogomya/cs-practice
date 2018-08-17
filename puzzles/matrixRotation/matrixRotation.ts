type Matrix<T> = T[][];

function rotateMatrix<T>(matrix: Matrix<T>): Matrix<T> {
    const size = matrix.length;
    if(!size) {
        return matrix;
    }
    const rotatedMatrix: Matrix<T> = new Array(size).fill(undefined).map(() => []);
    for (let i=0; i<size/2; i++) {
        for (let j=0; j< size - i - 1; j++) {
            const temp = matrix[i][j];
            rotatedMatrix[i][j] = matrix[size-1-j][i]; // leftToTop;
            rotatedMatrix[size-1-j][i] = matrix[size-1-i][size-1-j]; // bottomToLeft;
            rotatedMatrix[size-1-i][size-1-j] = matrix[j][size-1-i]; // rightToBottom
            rotatedMatrix[j][size-1-i] = temp; // topToRight
        }
    }
    if(size % 2) {
        const i = Math.ceil(size / 2) - 1;
        rotatedMatrix[i][i] = matrix[i][i];
    }

    return rotatedMatrix;
}

const source = [
    [ 1,  2,  3,  4,  5],
    [ 6,  7,  8,  9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
];

const output = [
    [21, 16, 11, 6, 1],
    [22, 17, 12, 7, 2],
    [23, 18, 13, 8, 3],
    [24, 19, 14, 9, 4],
    [25, 20, 15, 10, 5],
];

console.log(rotateMatrix(source).toString() === output.toString());

const source2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
];

const output2 = [
    [ 13, 9, 5, 1 ],
    [ 14, 10, 6, 2 ],
    [ 15, 11, 7, 3 ],
    [ 16, 12, 8, 4 ],
];

console.log(rotateMatrix(source2).toString() === output2.toString());

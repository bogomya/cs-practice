type Matrix<T> = T[][];

function rotateMatrix<T>(matrix: Matrix<T>): Matrix<T> {
    const size = matrix.length;
    if(!size) {
        return matrix;
    }
    const rotatedMatrix = Array(size).fill(undefined).map(() => []);
    for (let i=0; i<size/2; i++) {
        const first = i;
        const last = size - i - 1;
        for (let j=first; j<=last; j++) {
            rotatedMatrix[j][last] = matrix[i][j]; // topToRight
            rotatedMatrix[last][last-j+i] = matrix[j][last]; // rightToBottom
            rotatedMatrix[j][first] = matrix[last][j]; // bottomToLeft;
            rotatedMatrix[first][last-j+i] = matrix[j][first]; // leftToTop;
        }
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
]

console.log(rotateMatrix(source2).toString() === output2.toString());

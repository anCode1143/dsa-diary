class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix
        self.prefix = []
        for row in range(len(matrix) + 1):
            prefixRow = []
            for col in range(len(matrix[0]) + 1):
                if row == 0 or col == 0:
                    prefixRow.append(0)
                else:
                    prefixRow.append(prefixRow[-1] + self.prefix[row-1][col] - self.prefix[row-1][col-1] + matrix[row-1][col-1])
            self.prefix.append(prefixRow)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        leftRec = self.prefix[row2+1][col1]
        rightRec = self.prefix[row1][col2+1]
        return self.prefix[row2+1][col2+1] - leftRec - rightRec + self.prefix[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
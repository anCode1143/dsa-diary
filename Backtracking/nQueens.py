from typing import List

def solveNQueens(n: int) -> List[List[str]]:
    def overlaps(board, row, col):
        for variable in range(n):
            if board[variable][col] == 'Q' or board[row][variable] == 'Q':
                return True
        def checkDiagonal(rowCounter, colCounter):
            rowDiagonal, colDiagonal = row + rowCounter, col + colCounter
            while 0 <= rowDiagonal < n and 0 <= colDiagonal < n:
                if board[rowDiagonal][colDiagonal] == 'Q':
                    return True
                rowDiagonal += rowCounter
                colDiagonal += colCounter
            return False
        if (checkDiagonal(1, 1) or checkDiagonal(-1, 1) 
            or checkDiagonal(-1, -1) or checkDiagonal(1, -1)):
            return True
        return False
    def backtrack(answers, currBoard, startRow):
        if startRow == n:
            answers.append([row.copy() for row in currBoard])
            return
        for col in range(n):
            if not overlaps(currBoard, startRow, col):
                currBoard[startRow][col] = 'Q'
                backtrack(answers, currBoard, startRow + 1)
                currBoard[startRow][col] = '.'

    board = [['.' for _ in range(n)] for _ in range(n)]
    answers = []
    backtrack(answers, board, 0)
    print("Number of raw answers found:", len(answers))
    for index, answer in enumerate(answers):
        newAnswer = []
        for row in range(n):
            newAnswer.append(''.join(answer[row]))
        answers[index] = newAnswer
    return answers

print(solveNQueens(4))
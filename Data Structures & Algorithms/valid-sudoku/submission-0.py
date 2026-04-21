class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for row in range(9):
            unique = set()
            for j in range(9):
                if board[row][j] == ".":
                    continue
                elif board[row][j] in unique:
                    return False
                unique.add(board[row][j])
        
        # check columns
        for col in range(9):
            unique = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                elif board[i][col] in unique:
                    return False
                unique.add(board[i][col])
        
        # check grid
        for square in range(9):
            unique = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    elif board[row][col] in unique:
                        return False
                    unique.add(board[row][col])
        return True
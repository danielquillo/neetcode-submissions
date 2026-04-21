class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # BRUTE FORCE SOLUTION
        # check rows
        # for row in range(9):
        #     unique = set()
        #     for j in range(9):
        #         if board[row][j] == ".":
        #             continue
        #         elif board[row][j] in unique:
        #             return False
        #         unique.add(board[row][j])
        # check columns
        # for col in range(9):
        #     unique = set()
        #     for i in range(9):
        #         if board[i][col] == ".":
        #             continue
        #         elif board[i][col] in unique:
        #             return False
        #         unique.add(board[i][col])
        # check grid
        # for square in range(9):
        #     unique = set()
        #     for i in range(3):
        #         for j in range(3):
        #             row = (square // 3) * 3 + i
        #             col = (square % 3) * 3 + j
        #             if board[row][col] == ".":
        #                 continue
        #             elif board[row][col] in unique:
        #                 return False
        #             unique.add(board[row][col])
        # return True

        # ONE PASS HASH SET SOLUTION
        cols = defaultdict(set)
        rows    = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if ( board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True
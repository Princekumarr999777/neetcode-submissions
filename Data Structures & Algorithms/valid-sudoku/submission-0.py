class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            for j in range(9):

                no_to_check = board[i][j]

                if no_to_check == ".":
                    continue

                # row check
                for k in range(9):

                    if j != k and no_to_check == board[i][k]:
                        return False

                # column check
                for m in range(9):

                    if i != m and no_to_check == board[m][j]:
                        return False

                # 3x3 grid check
                start_row = (i // 3) * 3
                start_col = (j // 3) * 3

                for r in range(start_row, start_row + 3):
                    for c in range(start_col, start_col + 3):

                        if (r != i or c != j) and board[r][c] == no_to_check:
                            return False

        return True
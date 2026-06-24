class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {i: set() for i in range(0, 10)}
        col = {i: set() for i in range(0, 10)}
        sq = {i: set() for i in range(0, 10)}
        n = len(board)
        for r in range(n):
            for c in range(n):
                ch = board[r][c]
                square_idx = r//3 * 3 + c//3
                if not ch.isnumeric():
                    continue
                else:
                    if ch in row[r] or ch in col[c] or ch in sq[square_idx]:
                        return False
                    row[r].add(ch)
                    col[c].add(ch)
                    sq[square_idx].add(ch)
            
        return True
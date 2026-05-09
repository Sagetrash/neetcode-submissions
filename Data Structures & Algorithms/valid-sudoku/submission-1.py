class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {}
        col = {}
        square = {}
        n = 9
        for i in range(n):
            for j in range(n):
                curr = board[i][j]
                if curr == '.':
                    continue
                if curr in row.setdefault(i,set()) or curr in col.setdefault(j,set()) or curr in square.setdefault((i//3,j//3),set()):
                    return False
                row[i].add(curr)
                col[j].add(curr)
                square[(i//3,j//3)].add(curr)
        return True
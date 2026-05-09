class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)
        n = 9
        for i in range(n):
            for j in range(n):
                curr = board[i][j]
                if curr == '.':
                    continue
                if curr in row[i] or curr in col[j] or curr in square[(i//3,j//3)]:
                    return False
                row[i].add(curr)
                col[j].add(curr)
                square[(i//3,j//3)].add(curr)
        return True
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqs = defaultdict(set)

        for r in range(9):
            for c in range(9):
                curr = board[r][c]
                if board[r][c] == ".":
                    continue
                elif (curr in rows[r]) or (curr in cols[c]) or (curr in sqs[(r//3,c//3)]):
                    return False
                rows[r].add(curr)
                cols[c].add(curr)
                sqs[(r//3,c//3)].add(curr)
        return True
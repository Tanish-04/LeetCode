class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Defining dictionary of sets
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        blocks = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                
                if board[r][c] == '.':
                    continue
                
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in blocks[(r//3)*3,c//3]):
                    return False
                
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                blocks[(r//3)*3,c//3].add(board[r][c])
                
        return True
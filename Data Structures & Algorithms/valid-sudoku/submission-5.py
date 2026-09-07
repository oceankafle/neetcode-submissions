class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set) # {coord: (set)}
        cols = defaultdict(set)
        subboards = defaultdict(set)

        for r in range(9): # can simply loop through 9 because the board's dimentions are fixed
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if (board[r][c] in rows[r] or
                board[r][c] in cols[c] or
                board[r][c] in subboards[(r//3, c//3)]):
                    return False
                
                # the case where the number is valid and can be successfully added to all 3 dicts
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                subboards[(r//3, c//3)].add(board[r][c])
        
        return True

        


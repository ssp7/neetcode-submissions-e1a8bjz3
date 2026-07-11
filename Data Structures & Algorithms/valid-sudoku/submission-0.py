class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(len(board)):
            for c in range(len(board[r])):
                if (not self.isRowValid(board, r) or 
                    not self.isColValid(board, c) or 
                    not self.isQuadrantValid(board, r, c)):
                    print(r, c)
                    return False
        return True

    def isRowValid(self, board, r):
        s = set()
        for c in range(len(board[r])):
            val = board[r][c]
            if val != "." and val in s:
                return False
            s.add(val)

        return True
    
    def isColValid(self, board, c):
        s = set()
        for r in range(len(board)):
            val = board[r][c]
            if val != "." and val in s:
                return False
            s.add(val)
        return True
    
    def isQuadrantValid(self, board, r, c):
        s = set()
        r = (r // 3) * 3
        c = (c // 3) * 3

        for idx in range(3):
            for jdx in range(3):
                val = board[r + idx][c + jdx]
                if val != "." and val in s:
                    return False
                s.add(val)
        
        return True
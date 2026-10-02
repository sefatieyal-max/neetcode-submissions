class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()
        def travel(i,j,charIndex):
            if charIndex == len(word):
                return True
            if i >= rows or i < 0 or j < 0 or j >= cols or word[charIndex] != board[i][j] or (i,j) in path:
                return False
            path.add((i,j))
            left = travel(i-1,j,charIndex+1)
            right = travel(i+1,j,charIndex+1)
            up = travel(i,j-1,charIndex+1)
            down = travel(i,j+1,charIndex+1)
            path.remove((i,j))
            return left or right or up or down
            
        for i in range(rows):
            for j in range(cols):
                if travel(i,j,0): return True

        return False
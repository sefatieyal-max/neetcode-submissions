class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, alt = set(), set()


        def dfs(r, c, visit, prevHeight):
            if r < 0 or r == rows or c < 0 or c == cols or (r,c) in visit or heights[r][c] < prevHeight:
                return
            visit.add((r,c))
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr,nc,visit,heights[r][c])

        #first and last row
        for col in range(cols):
            dfs(0, col, pac, heights[0][col])
            dfs(rows-1,col,alt,heights[rows-1][col])
        #first and last col
        for row in range(rows):
            dfs(row, 0, pac, heights[row][0])
            dfs(row, cols-1, alt, heights[row][cols-1])

        #find result
        res = []
        for c in range(cols):
            for r in range(rows):
                if (r,c) in pac and (r,c) in alt:
                    res.append([r,c])
        return res

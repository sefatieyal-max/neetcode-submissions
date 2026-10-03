class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r,c):
            q = deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                nr, nc = q.popleft()
                directios = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr,dc in directios:
                    row, col = nr + dr, nc + dc
                    if row in range(rows) and col in range(cols) and (row,col) not in visit and grid[row][col] == "1":
                        visit.add((row,col))
                        q.append((row,col))
                        


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1
        return islands

        
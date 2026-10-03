class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if n-1 != len(edges):
            return False

        neighbors = {i : [] for i in range(n)}
        for i, j in edges:
            neighbors[i].append(j)
            neighbors[j].append(i)

        visit = set()

        def dfs(node):
            if node in visit:
                return False
            if neighbors[node] == []:
                return True
            visit.add(node)
            for neighbor in neighbors[node]:
                neighbors[neighbor].remove(node)
                if not dfs(neighbor): return False
            visit.remove(node)
            neighbors[node] = []
            return True

        for node in range(n):
            if not dfs(node): return False
        return True
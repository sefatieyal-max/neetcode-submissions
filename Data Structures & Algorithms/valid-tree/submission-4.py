class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if not n:
            return True

        if n-1 != len(edges):
            return False

        neighbors = {i : [] for i in range(n)}
        for i, j in edges:
            neighbors[i].append(j)
            neighbors[j].append(i)

        visit = set()

        def dfs(node, prev):
            if node in visit:
                return False
            visit.add(node)

            for neighbor in neighbors[node]:
                if neighbor == prev:
                    continue
                if not dfs(neighbor,node): return False

            return True



        return dfs(0,-1) and len(visit) == n
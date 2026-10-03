class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        neighbors ={i : [] for i in range(n)}
        for n1, n2 in edges:
            neighbors[n1].append(n2)
            neighbors[n2].append(n1)
            
        visit = set()

        def dfs(node, prev):
            if node in visit:
                return
            visit.add(node)
            for i in neighbors[node]:
                if i != prev:
                    dfs(i,node)

        res = 0
        for i in range(n):
            if i not in visit:
                res += 1
                dfs(i,-1)

        return res
        

        
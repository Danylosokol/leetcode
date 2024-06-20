class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i:[] for i in range(numCourses)}

        for pre, crs in prerequisites:
            adj[crs].append(pre)
        
        preHashmap = {}

        def dfs(crs):
            if crs not in preHashmap:
                preHashmap[crs] = set()
                for pre in adj[crs]:
                    preHashmap[crs] |= dfs(pre)
                preHashmap[crs].add(crs)
            return preHashmap[crs]
            
        for crs in adj:
            dfs(crs)

        result = []
        for u, v in queries:
            result.append(u in preHashmap[v])
        
        return result

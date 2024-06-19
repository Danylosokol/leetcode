class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i: [] for i in range(numCourses)}

        for pre, crs in prerequisites:
            adj[crs].append(pre)
        
        prereqMap = {}

        def dfs(crs):
            if crs not in prereqMap:
                prereqMap[crs] = set()
                for pre in adj[crs]:
                    prereqMap[crs] |= dfs(pre)
                prereqMap[crs].add(crs)
            return prereqMap[crs]

        for crs in adj:
            dfs(crs)

        result = []
        for u, v in queries:
            result.append(u in prereqMap[v])
        
        return result
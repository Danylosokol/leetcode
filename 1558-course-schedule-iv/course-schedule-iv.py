class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            adj[crs].append(pre)

        result = []

        for pre, crs in queries:
            visited = set()
            result.append(self.dfs(pre, crs, visited, adj))
        return result
        
    def dfs(self, pre, crs, visited, adj):
        if pre in visited:
            return False
        
        visited.add(pre)

        for i  in adj[pre]:
            self.dfs(i, crs, visited, adj)
        
        return crs in visited


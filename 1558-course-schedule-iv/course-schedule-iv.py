class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            adj[crs].append(pre)

        result = []

        for pre, crs in queries:
            visited = set()
            top_sort = set()
            self.dfs(pre, visited, adj, top_sort)
            if crs in top_sort:
                result.append(True)
            else:
                result.append(False)
        return result
        
    def dfs(self, crs, visited, adj, top_sort):
        if crs in visited:
            return False
        
        visited.add(crs)

        for pre in adj[crs]:
            self.dfs(pre, visited, adj, top_sort)
        
        top_sort.add(crs)


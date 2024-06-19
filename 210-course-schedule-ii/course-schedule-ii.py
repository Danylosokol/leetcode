class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}
        
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        top_sort = []
        visited = set()
        path = set()

        for crs in adj:
            if not self.dfs(crs, visited, path, adj, top_sort):
                return []
        
        return top_sort
    
    def dfs(self, crs, visited, path, adj, top_sort):
        if crs in path:
            return False
        
        if crs in visited:
            return True
        
        visited.add(crs)
        path.add(crs)

        for pre in adj[crs]:
            if not self.dfs(pre, visited, path, adj, top_sort):
                return False
        
        path.remove(crs)
        top_sort.append(crs)
        return True
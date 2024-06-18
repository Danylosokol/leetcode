class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        topSort = []
        path = set()
        visited = set()

        for crs in adj:
            if not self.dfs(crs, adj, visited, path, topSort):
                return []
        return topSort
    
    def dfs(self, crs, adj, visited, path, topSort):
        if crs in path:
            return False
        
        if crs in visited:
            return True
        
        visited.add(crs)
        path.add(crs)

        for pre in adj[crs]:
            if not self.dfs(pre, adj, visited, path, topSort):
                return False
        
        topSort.append(crs)
        path.remove(crs)
        return True
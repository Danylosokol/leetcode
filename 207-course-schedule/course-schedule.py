class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}

        for i in range(numCourses):
            adj[i] = []
        
        for dst, src in prerequisites:
            adj[src].append(dst)

        topSort = []
        visited = set()
        path = set()
        for i in adj:
            if not self.dfs(i, adj, visited, path, topSort):
                return False

        return True        
    
    def dfs(self, src, adj, visited, path, topSort):
        if src in path:
            return False

        if src in visited:
            return True

        visited.add(src)
        path.add(src)

        for dst in adj[src]:
            if not self.dfs(dst, adj, visited, path, topSort):
                return False
        
        topSort.append(src)
        path.remove(src)
        return True
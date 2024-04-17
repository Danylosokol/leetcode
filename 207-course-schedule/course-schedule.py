class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        
        takenCourses = 0

        def dfs_check(parent, child, graph, visited):
            visited.append(parent)
            if child in graph[parent]:
                return True
            result = False
            for node in graph[parent]:
                if node in visited:
                    continue
                result = dfs_check(node, child, graph, visited)
                if result:
                    return result
            
            return result

        for node in prerequisites:
            if node[0] not in graph:
                graph[node[0]] = []
                takenCourses += 1
                if takenCourses > numCourses:
                    return False
            if node[1] not in graph:
                graph[node[1]] = []
                takenCourses += 1
                if takenCourses > numCourses:
                    return False
            if node[0] == node[1] or dfs_check(node[1], node[0], graph, []):
                return False
            graph[node[0]].append(node[1])
        return True
    

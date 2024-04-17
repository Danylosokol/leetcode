class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashMap = {i:[] for i in range(numCourses)}

        for course, prereq in prerequisites:
            hashMap[course].append(prereq)
        
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            
            if hashMap[course] == []:
                return True
            
            visited.add(course)
            for prereq in hashMap[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            hashMap[course] = []
            return True
        
        for course in hashMap:
            if not dfs(course):
                return False
        
        return True
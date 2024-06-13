class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {}

        for i in range(len(points)):
            adj[i] = []
        
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                distance = abs(points[j][0] - points[i][0]) + abs(points[j][1] - points[i][1])
                adj[i].append((distance, j))
                adj[j].append((distance, i))
        
        min_heap = []
        visited = set()

        for distance, neighbour in adj[0]:
            heapq.heappush(min_heap, [distance, 0, neighbour])

        visited.add(0)
        result = 0

        while min_heap:
            d1, s1, n1 = heapq.heappop(min_heap)

            if n1 in visited:
                continue
            
            result += d1
            visited.add(n1)

            for d2, n2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(min_heap, [d2, n1, n2])
        
        return result


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []

        for point in points:
            dist = point[0]**2 + point[1]**2
            min_heap.append((dist, point))
        
        heapq.heapify(min_heap)

        result = []
        while k > 0:
            result.append(heapq.heappop(min_heap)[1])
            k -= 1

        return result
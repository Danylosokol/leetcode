class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            distnace = point[0]**2 + point[1]**2
            heap.append((distnace, point))
        
        heapq.heapify(heap)
        result = []

        while k > 0:
            result.append(heapq.heappop(heap)[1])
            k -= 1
        
        return result
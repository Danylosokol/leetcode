class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        origin = [0, 0]
        for point in points:
            heapq.heappush(heap, (self.distance(origin, point), point))
        res = []
        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        
        return res

    def distance(self, point_1, point_2):
        return sqrt((point_1[0] - point_2[0])**2 + (point_1[1] - point_2[1])**2)
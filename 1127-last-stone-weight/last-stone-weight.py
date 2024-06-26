class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stone_1 = heapq.heappop(stones)
            stone_2 = heapq.heappop(stones)

            if stone_1 - stone_2 < 0:
                heapq.heappush(stones, stone_1 - stone_2)
            
        return heapq.heappop(stones) * -1 if len(stones) else 0
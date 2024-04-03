class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq._heapify_max(stones)
        while len(stones) > 1:
            stone_1 = heapq._heappop_max(stones)
            stone_2 = heapq._heappop_max(stones)
            if stone_1 - stone_2 > 0:
                stones.append(stone_1 - stone_2)
                heapq._heapify_max(stones)
        return heapq._heappop_max(stones) if len(stones) > 0 else 0
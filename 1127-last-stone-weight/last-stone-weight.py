class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq._heapify_max(stones)
        print("stones after heapify:")
        print(stones)
        while len(stones) > 1:
            stone_1 = heapq._heappop_max(stones)
            stone_2 = heapq._heappop_max(stones)
            print("stone_1:")
            print(stone_1)
            print("stone_2:")
            print(stone_2)
            print("current stones:")
            print(stones)
            print("length:")
            print(len(stones))
            print("--------------")
            if stone_1 - stone_2 > 0:
                heapq.heappush(stones, stone_1 - stone_2)
                heapq._heapify_max(stones)
        return heapq._heappop_max(stones) if len(stones) > 0 else 0
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n + 1):
            adj[i] = []

        for s, d, w in times:
            adj[s].append((w, d))
        
        minHeap = [(0, k)]
        shortest = {}

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue
            shortest[n1] = w1

            for w2, n2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, (w2 + w1, n2))
        
        result = max(shortest.values())
        return result if result and len(shortest) == n else -1
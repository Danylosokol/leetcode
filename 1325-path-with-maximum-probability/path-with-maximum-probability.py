class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {}
        for i in range(n):
            adj[i] = []

        for i in range(len(edges)):
            adj[edges[i][0]].append((succProb[i], edges[i][1]))
            adj[edges[i][1]].append((succProb[i], edges[i][0]))
        
        maxHeap = [(-1, start_node)]
        result = {}

        while maxHeap:
            w1, n1 = heapq.heappop(maxHeap)
            w1 *= -1

            if n1 in result:
                continue

            result[n1] = w1

            for w2, n2 in adj[n1]:
                if n2 not in result:
                    heapq.heappush(maxHeap, (w2 * w1 * -1, n2))

        return result[end_node] if end_node in result else 0

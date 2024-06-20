class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        def topological_sort(degrees, graph, items):
            queue = deque([item for item in items if degrees[item] == 0])
            result = []
            while queue:
                current = queue.popleft()
                result.append(current)
                for neighbour in graph[current]:
                    degrees[neighbour] -= 1
                    if degrees[neighbour] == 0:
                        queue.append(neighbour)
            return result if len(result) == len(items) else []
        
        index = m
        group_to_items = [[] for _ in range(n + m)]
        for item, grp in enumerate(group):
            if grp == -1:
                group[item] = index
                index += 1
            group_to_items[group[item]].append(item)
        
        item_degree = [0] * n
        group_degree = [0] * (n + m)
        item_graph = [[] for _ in range(n)]
        group_graph = [[] for _ in range(n + m)]

        for i, gi in enumerate(group):
            for j in beforeItems[i]:
                gj = group[j]
                if gi == gj:
                    item_degree[i] += 1
                    item_graph[j].append(i)
                else:
                    if gi not in group_graph[gj]:
                        group_degree[gi] += 1
                        group_graph[gj].append(gi)

        group_order = topological_sort(group_degree, group_graph, list(range(n + m)))
        if not group_order:
            return []
        
        final_order = []

        for group_index in group_order:
            items_in_group = group_to_items[group_index]
            item_order = topological_sort(item_degree, item_graph, items_in_group)
            if len(items_in_group) != len(item_order):
                return []
            final_order.extend(item_order)
        
        return final_order
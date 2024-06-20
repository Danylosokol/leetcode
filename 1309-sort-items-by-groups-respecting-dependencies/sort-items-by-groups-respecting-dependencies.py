from collections import deque  # importing deque from collections for queue functionality

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # Function to perform topological sort
        def topological_sort(degrees, graph, items):
            # Initialize a queue with items that have no prerequisites (degree = 0)
            queue = deque([item for item in items if degrees[item] == 0])
            result = []
            while queue:
                current = queue.popleft()
                result.append(current)
                for neighbor in graph[current]:
                    # Decrement the degree of neighboring items since current is processed
                    degrees[neighbor] -= 1
                    # If neighbor's degree is zero, add it to the queue
                    if degrees[neighbor] == 0:
                        queue.append(neighbor)
            # Check whether we have sorted all the items
            return result if len(result) == len(items) else []

        # Assign each standalone item (-1 group) a unique group number
        index = m
        group_to_items = [[] for _ in range(n + m)]
        for item, grp in enumerate(group):
            if grp == -1:
                group[item] = index
                index += 1
            group_to_items[group[item]].append(item)

        # Initialize degrees and graphs for items and groups
        item_degree = [0] * n
        group_degree = [0] * (n + m)
        item_graph = [[] for _ in range(n)]
        group_graph = [[] for _ in range(n + m)]
      
        # Build graphs and compute degrees for items and groups
        for i, gi in enumerate(group):
            for j in beforeItems[i]:
                gj = group[j]
                if gi == gj:
                    # Same group; add edge in item graph and update item degree
                    item_degree[i] += 1
                    item_graph[j].append(i)
                else:
                    # Different groups; add edge in group graph and update group degree
                    if gi not in group_graph[gj]:
                        group_degree[gi] += 1
                        group_graph[gj].append(gi)

        # Perform topological sort on the groups
        group_order = topological_sort(group_degree, group_graph, list(range(n + m)))
        if not group_order:
            return []  # if sorting fails, return empty list
      
        final_order = []  # final sorted order of items to return
      
        # For each group in the sorted order, perform topological sort on its items
        for group_index in group_order:
            items_in_group = group_to_items[group_index]
            item_order = topological_sort(item_degree, item_graph, items_in_group)
            if len(items_in_group) != len(item_order):
                return []  # if sorting fails for items within the group, return empty list
            final_order.extend(item_order)  # append the successfully sorted items to final order
      
        return final_order  # return the final topologically sorted order of all items
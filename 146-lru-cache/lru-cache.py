class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cash = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
    
    def insert_right(self, node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.prev, node.next = prev, next

    def get(self, key: int) -> int:
        if key in self.cash:
            self.remove(self.cash[key])
            self.insert_right(self.cash[key])
            return self.cash[key].val
        else:
            return - 1

    def put(self, key: int, value: int) -> None:
        if key in self.cash:
            self.remove(self.cash[key])
        self.cash[key] = Node(key, value)
        self.insert_right(self.cash[key])

        if len(self.cash) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cash[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = Node(start, end)
            return True
        return self.search(self.root, start, end)
    
    def search(self, root, start, end, parent=None):
        if root:
            if end > root.start and start < root.end:
                return False
            elif end <= root.start:
                return self.search(root.left, start, end, root)
            else:
                return self.search(root.right, start, end, root)
        else:
            return self.update(parent, start, end)

    def update(self, parent, start, end):
        if end <= parent.start:
            parent.left = Node(start, end)
        else:
            parent.right = Node(start, end)
        return True           


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
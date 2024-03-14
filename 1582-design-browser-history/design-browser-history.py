class ListNode():
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.left = ListNode(homepage)
        self.right = ListNode(-1)
        self.left.next = self.right
        self.right.prev = self.left
        self.curr = self.left  

    def visit(self, url: str) -> None:
        new_node = ListNode(url)
        prev = self.curr
        next = self.right
        prev.next = new_node
        next.prev = new_node
        new_node.prev = prev
        new_node.next = next
        self.curr = new_node

    def back(self, steps: int) -> str:
        curr = self.curr
        while curr != self.left and steps > 0:
            curr = curr.prev
            steps -= 1
        self.curr = curr
        return curr.val

    def forward(self, steps: int) -> str:
        curr = self.curr
        while curr.next != self.right and steps > 0:
            curr = curr.next
            steps -= 1
        self.curr = curr
        return curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
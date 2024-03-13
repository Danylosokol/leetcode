class ListNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.left = ListNode(-1)
        self.right = ListNode(-1)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        curr = self.left.next
        while curr:
            if index == 0:
                return curr.val
            curr = curr.next
            index -= 1
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        prev = self.left
        next = self.left.next
        prev.next = new_node
        new_node.prev = prev
        next.prev = new_node
        new_node.next = next

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        next = self.right
        prev = self.right.prev
        prev.next = new_node
        new_node.prev = prev
        next.prev = new_node
        new_node.next = next

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.left

        while curr.next and index != 0:
            curr = curr.next
            index -= 1
        
        if curr.next and index == 0:
            prev = curr
            next = curr.next
            new_node = ListNode(val)
            prev.next = new_node
            new_node.prev = prev
            next.prev = new_node
            new_node.next = next

    def deleteAtIndex(self, index: int) -> None:
        curr = self.left

        while curr.next != self.right and index != 0:
            curr = curr.next
            index -= 1
        
        if curr.next != self.right and index == 0:
            prev = curr
            next = curr.next.next
            prev.next = next
            next.prev = prev


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
        

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                print(f"at index: {index} value: {curr.val}")
                return curr.val
            curr = curr.next
            i += 1
        return -1
        

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if new_node.next == None:
            print("updating tail...")
            self.tail = new_node

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = new_node
        # print("new tail:")
        # print(self.tail.val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = ListNode(val)
        curr = self.head
        i = 0
        while i < index and curr:
            curr = curr.next
            i += 1
        if curr:
            new_node.next = curr.next
            curr.next = new_node
            print("adding new node:")
            print(new_node.val)
            print("new node pointer:")
            print(new_node.next)
            if new_node.next == None:
                print("updating tail...")
                self.tail = new_node

    def deleteAtIndex(self, index: int) -> None:
        print(f"deleting at index: {index}")
        curr = self.head
        i = 0
        while i < index and curr.next:
            print("curr value in a loop:")
            print(curr.val)
            curr = curr.next
            i += 1
        if curr.next and i == index:
            # print("current value:")
            # print(curr.val)
            # print("next curr value:")
            # print(curr.next.val)
            curr.next = curr.next.next
            if curr.next == None:
                self.tail = curr
            # print("next curr value after update:")
            # print(curr.next.val)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
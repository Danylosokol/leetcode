# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_node = head
        if not curr_node:
            return curr_node
        unlinked_node = curr_node.next
        while curr_node:
            print(curr_node.val)
            next_node = unlinked_node
            if curr_node == head:
                curr_node.next = None
            if next_node == None:
                print("in the end of the list")
                print(curr_node.val)
                break
            unlinked_node = next_node.next
            next_node.next = curr_node
            curr_node = next_node
        return curr_node
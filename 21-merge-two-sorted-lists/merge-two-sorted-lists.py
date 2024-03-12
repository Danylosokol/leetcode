# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2 or not list2:
            return list1 
        elif not list1:
            return list2

        if list1.val < list2.val:
            prev = list1
            list1 = list1.next
        else:
            prev = list2
            list2 = list2.next

        new_head = prev
    
        while list1 and list2:
            if list1.val < list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next 
            prev = prev.next

        if not list1:
            prev.next = list2
        else:
            prev.next = list1
        return new_head
        
            
                
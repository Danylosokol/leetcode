# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(left_pointer, right_pointer) -> [ListNode]:
            result = ListNode(None)
            result_head = result

            while left_pointer != None and right_pointer != None:
                if left_pointer.val <= right_pointer.val:
                    result.next = left_pointer
                    result = result.next
                    left_pointer = left_pointer.next
                else:
                    result.next = right_pointer
                    result = result.next
                    right_pointer = right_pointer.next

            if left_pointer == None:
                result.next = right_pointer
            else:
                result.next = left_pointer
            return result_head.next

            
        if not lists:
            return

        final_result = lists[0]
        for i in range(1, len(lists)):
            final_result = merge(final_result, lists[i])
        return final_result

        
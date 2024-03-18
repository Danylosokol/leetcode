# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(left_pointer, right_pointer) -> [ListNode]:
            # print("in merge:")
            # print("left_pointer:")
            # print(left_pointer)
            # print("right_pointer:")
            # print(right_pointer)
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
                # print("assigning result to left_pointer")
                result.next = right_pointer
            else:
                # print("assigning result to right pointer")
                result.next = left_pointer
            # print("result in the end:")
            # print(result)
            # print("result header is:")
            # print(result_head)
            return result_head.next
        
        final_result = None
        for i in range(len(lists)):
            final_result = merge(final_result, lists[i])
        return final_result

        
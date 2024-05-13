# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        prevSlow = None

        while fast and fast.next:
            fast = fast.next.next
            temp = slow
            slow = slow.next
            temp.next = prevSlow
            prevSlow = temp

        maxSum = 0
        while slow:
            currSum = prevSlow.val + slow.val
            print("slow: " + str(slow.val))
            print("prevSlow: " + str(prevSlow.val))
            maxSum = max(currSum, maxSum)
            prevSlow = prevSlow.next
            slow = slow.next
        
        return maxSum
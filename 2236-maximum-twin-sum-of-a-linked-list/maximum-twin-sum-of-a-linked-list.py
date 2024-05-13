# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        history = []

        while fast and fast.next:
            fast = fast.next.next
            history.append(slow.val)
            slow = slow.next
        
        maxSum = 0
        i = len(history) - 1
        while slow:
            currSum = history[i] + slow.val
            print("sum of:")
            print(str(history[i]) + " + " + str(slow.val))
            print(currSum) 
            maxSum = max(currSum, maxSum)
            slow = slow.next
            i -= 1
        
        return maxSum

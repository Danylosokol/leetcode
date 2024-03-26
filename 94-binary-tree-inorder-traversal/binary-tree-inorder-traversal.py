# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result, stack = [], []
        curr = root

        while curr or stack:
            while curr:
                print("adding to stack:")
                print(curr.val)
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            print("popping from the stack and adding to the result array:")
            print(curr.val)
            result.append(curr.val)
            curr = curr.right
        
        return result
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = collections.deque()
        result = []

        if root:
            queue.append(root)
        
        while queue:
            right_most = None

            for _ in range(len(queue)):
                node = queue.popleft()
                right_most = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if right_most:
                result.append(right_most.val)
        
        return result
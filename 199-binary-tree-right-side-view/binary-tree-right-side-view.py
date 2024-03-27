# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        queue = collections.deque()

        if root:
            queue.append(root)

        while len(queue):
            print("level.....")
            print(len(queue))
            queueLen = len(queue)
            for i in range(queueLen):
                node = queue.popleft()
                print(node)
                if i == queueLen - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result
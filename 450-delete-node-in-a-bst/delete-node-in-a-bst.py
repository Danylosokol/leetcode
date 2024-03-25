# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        print("deleting:")
        print(key)
        if not root:
            return None
        print("curr val:")
        print(root.val)
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left == None:
                print('root.left == None')
                return root.right
            elif root.right == None:
                print('root.right == None')
                return root.left
            else:
                minNode = self.findMin(root.right)
                print("min node val")
                print(minNode.val)
                print("root val:")
                print(root.val)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)
                print("new root right:")
                print(root.right)
        print("after all checks return root:")
        print(root.val)
        return root

    def findMin(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = root

        while curr.left:
            curr = curr.left
        
        return curr
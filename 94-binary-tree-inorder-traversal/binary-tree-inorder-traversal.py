# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        print(root)
        travers = []

        def traversal(root):
            
            if (root.left is None) and root.right is None:
                travers.append(root.val)
            elif root.left is None and root.right is not None:
                travers.append(root.val)
                traversal(root.right)
            elif root.left is not None and root.right is None:
                traversal(root.left)
                travers.append(root.val)
            else:
                traversal(root.left)
                travers.append(root.val)
                traversal(root.right)

        traversal(root)
        return travers
        
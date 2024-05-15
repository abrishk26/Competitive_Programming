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

        trav = []
        if root.left is None and root.right is None:
            trav.append(root.val)
            return trav
        
        trav += self.inorderTraversal(root.left)
        
        trav.append(root.val)
        
        trav += self.inorderTraversal(root.right)
        
        return trav
            
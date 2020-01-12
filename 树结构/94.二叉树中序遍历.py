#二叉树遍历基础题

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return [] 
        else:
            LDRlist = []
            LDRlist = LDRlist + self.inorderTraversal(root.left)
            LDRlist.append(root.val)
            LDRlist = LDRlist + self.inorderTraversal(root.right)

            return LDRlist
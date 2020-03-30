#DFS遍历节点

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None

        def recursenode(currentnode):
            if not currentnode:
                return False
            
            left = recursenode(currentnode.left)

            right = recursenode(currentnode.right)

            mid  = currentnode == p or currentnode == q

            if left + right + mid >=2:
                self.ans = currentnode

            return left or right or mid

        
        recursenode(root)

        return self.ans
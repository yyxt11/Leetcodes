#确保左边子节点恒小于当前节点和父节点的值, 右边子节点恒大于当前节点和父节点的值

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        
        def search(root:TreeNode,lowbonde = float('-inf'),highbonde = float('inf')):

            if root is None:
                return True
            else:
                if root.val <= lowbonde or root.val >=  highbonde:
                    return False
                #recall
                elif not search(root.left,lowbonde,root.val):
                    return False
                elif not search(root.right,root.val,highbonde):
                    return False

            return True

        return search(root)
        

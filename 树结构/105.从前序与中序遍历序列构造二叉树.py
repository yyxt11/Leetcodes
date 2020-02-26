#1.定位中间root节点（前序遍历的首节点），
#2.通过找到root节点的切分左右树节点（中序遍历中root节点的位置，切分左边树节点和右边树节点）
#3.递归实现
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        
        x = preorder.pop(0)
        node =TreeNode(x)

        #左右树分割点，递归执行以下的操作
        index = inorder.index(x)


        node.left = self.buildTree(preorder[:index],inorder[:index])
        node.right = self.buildTree(preorder[index:],inorder[index+1:])

        return node


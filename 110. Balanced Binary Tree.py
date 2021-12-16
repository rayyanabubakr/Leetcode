# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:

# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.balance = True
        self.check(root)
        return self.balance
        
    def check(self,v:TreeNode):
        if v == None:
            return 0
        if (v.left == None) & (v.right == None):
            return 1
        left = self.check(v.left)
        right = self.check(v.right)
        
        if abs(left - right) > 1:
            self.balance = False
        return max(left,right) + 1

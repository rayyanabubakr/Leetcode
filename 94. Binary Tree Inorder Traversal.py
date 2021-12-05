# Given the root of a binary tree, return the inorder traversal of its nodes' values.

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
            self.ans = []
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.ans=[]
        self.solve(root)
        return self.ans
    def solve(self,root):
        if root is None:
            return
        self.solve(root.left)
        self.ans.append(root.val)
        self.solve(root.right)
    

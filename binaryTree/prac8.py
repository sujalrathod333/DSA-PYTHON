# 110 balanced binary tree
class Solution:
    def __init__(self):
        self.ans = True
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftNode=self.maxDepth(root.left)
        rightNode=self.maxDepth(root.right) 
        
        if abs(leftNode - rightNode ) > 1:
            self.ans=False
        
        return max(leftNode, rightNode) + 1 
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.maxDepth(root)
        return self.ans
        
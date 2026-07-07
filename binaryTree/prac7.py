#104 maximum depth of binary tree 
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftNode=self.maxDepth(root.left)
        rightNode=self.maxDepth(root.right) 
        return max(leftNode, rightNode) + 1 
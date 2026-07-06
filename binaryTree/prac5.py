# 107 binary tree ka level order traversal II
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            levelS = len(queue)
            levelV = []

            for _ in range(levelS):
                node = queue.pop(0)
                levelV.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(levelV)
        return result[::-1]
    
    
# Test karne ke liye tree banate hain: 1 -> (2, 3), 2 -> (4)
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

sol = Solution()
print(sol.levelOrder(root))
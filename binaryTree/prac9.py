#700 search in binary search tree
from typing import Optional
 
 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 
 
class Solution:
    def searchBST(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        curr = root
 
        while curr is not None:
            if curr.val == target:
                return curr
            elif curr.val < target:
                curr = curr.right
            else:
                curr = curr.left
 
        return None
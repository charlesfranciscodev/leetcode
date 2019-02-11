import math

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValidBST2(root, -math.inf, math.inf)
        
    def isValidBST2(self, root, min_value, max_value):
        if (root is None):
            return True
        if (root.val <= min_value):
            return False
        if (root.val >= max_value):
            return False
        return self.isValidBST2(root.left, min_value, root.val) and self.isValidBST2(root.right, root.val, max_value)

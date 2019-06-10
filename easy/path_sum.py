# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, target_sum: int) -> bool:
        if root is None:
            return False
        return self.recursive_has_path_sum(root, target_sum, 0)
        
    def recursive_has_path_sum(self, current_node, target_sum, current_sum):
        if current_node is None:
            return False
        current_sum += current_node.val
        if current_node.left is None and current_node.right is None:
            return current_sum == target_sum
        left_recursive_has_path_sum = self.recursive_has_path_sum(current_node.left, target_sum, current_sum)
        right_recursive_has_path_sum = self.recursive_has_path_sum(current_node.right, target_sum, current_sum)
        return left_recursive_has_path_sum or right_recursive_has_path_sum

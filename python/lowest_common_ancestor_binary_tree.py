"""
Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


from collections import deque


class Solution:
    def build_path(self, node, parents):
        stack = []
        while node:
            stack.append(node)
            node = parents.get(node)
        return stack

    def bfs(self, root, target_node):
        parents = {}
        queue = deque()
        queue.append(root)
        while queue:
            current_node = queue.popleft()
            if current_node.val == target_node.val:
                return self.build_path(target_node, parents)
            for node in (current_node.left, current_node.right):
                if node:
                    parents[node] = current_node
                    queue.append(node)
        return []

    def lowestCommonAncestor(self, root: 'TreeNode', node1: 'TreeNode', node2: 'TreeNode') -> 'TreeNode':
        path1 = self.bfs(root, node1)
        path2 = self.bfs(root, node2)
        lowest_common_ancestor = None

        while path1 and path2:
            ancestor1 = path1.pop()
            ancestor2 = path2.pop()
            if ancestor1.val == ancestor2.val:
                lowest_common_ancestor = ancestor1
            else:
                break

        return lowest_common_ancestor

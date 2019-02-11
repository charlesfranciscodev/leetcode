# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # breath-first search
        traversal = []
        distance = {}
        queue = deque()
        distance[root] = 0
        queue.append(root)
        
        if (root is None):
            return traversal
        
        while (len(queue) != 0):
            current = queue.popleft()
            if (distance[current] == len(traversal)):
                traversal.append([])
            traversal[distance[current]].append(current.val)
            traversal[distance[current] - 1] 
            children = [current.left, current.right]
            for child in children:
                if (child is not None):
                    distance[child] = distance[current] + 1
                    queue.append(child)
        
        return traversal

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_next_node = None
        current_node = head
        new_node = None
        while (current_node is not None):
            new_node = ListNode(current_node.val)
            new_node.next = new_next_node
            new_next_node = new_node
            current_node = current_node.next
        return new_node

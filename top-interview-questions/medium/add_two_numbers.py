# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        start_node = ListNode(None)
        current_node = start_node
        next_node = None
        carry = 0
        while (l1 is not None or l2 is not None):
            sum_vals = carry
            if (l1 is not None):
                sum_vals += l1.val
            if (l2 is not None):
                sum_vals += l2.val
            carry = sum_vals // 10
            if (sum_vals > 9):
                sum_vals -= carry * 10
            current_node.val = sum_vals
                
            if (l1 is not None):
                l1 = l1.next
            if (l2 is not None):
                l2 = l2.next
            if (l1 is None and l2 is None):
                if (carry != 0):
                    next_node = ListNode(carry)
                    current_node.next = next_node
            else:
                next_node = ListNode(None)
                current_node.next = next_node
                
            current_node = next_node
        return start_node

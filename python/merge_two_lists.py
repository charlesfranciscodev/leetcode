# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if (l1 is None and l2 is None):
            return None
        if (l2 is None or (l1 is not None and l1.val < l2.val)):
            start_node = ListNode(l1.val)
            current_node = start_node
            current1 = l1.next
            current2 = l2
        else:
            start_node = ListNode(l2.val)
            current_node = start_node
            current1 = l1
            current2 = l2.next
        
        while (current1 is not None or current2 is not None):
            if (current1 is not None and current2 is not None):
                if (current1.val < current2.val):
                    current_node.next = ListNode(current1.val)
                    current1 = current1.next
                else:
                    current_node.next = ListNode(current2.val)
                    current2 = current2.next
            elif (current1 is not None):
                current_node.next = ListNode(current1.val)
                current1 = current1.next
            else:
                current_node.next = ListNode(current2.val)
                current2 = current2.next
            current_node = current_node.next
        
        return start_node

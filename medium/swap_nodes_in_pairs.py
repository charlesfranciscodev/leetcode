# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        current = head
        while current is not None and current.next is not None:
            temp = current.val
            current.val = current.next.val
            current.next.val = temp
            current = current.next.next
        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        while current is not None:
            while current.next is not None and current.val == current.next.val:
                current.next = current.next.next
            current = current.next
        return head

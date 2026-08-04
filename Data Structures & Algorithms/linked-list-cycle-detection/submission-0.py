# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hs = set()
        curr = head

        while curr:
            if curr.next in hs:
                return True
            curr = curr.next
            hs.add(curr)

        return False
            
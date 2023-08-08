# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        slow = head
        fast = head
        # values = []
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # if fast.next is None:
        #     pass
        # else:
        #     slow = slow.next
        # while slow != None:
        #     values.append(slow.val)
        #     slow  = slow.next
        return slow
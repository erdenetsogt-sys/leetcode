# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        current = head
        return_node = head
        stack = []
        
        while current != None:
            stack.append(current.val)
            current = current.next

        while return_node != None:
            return_node.val = stack.pop()
            return_node = return_node.next
        
        return head
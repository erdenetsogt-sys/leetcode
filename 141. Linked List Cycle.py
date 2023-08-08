# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        if head.next is None:
            return False
        count = 0
        current = head
        second_current = head
        memory_addresses = []
        while current != None:
            if id(current) in memory_addresses:
                cycle_start = current
                return True
            memory_addresses.append(id(current))
            current = current.next
        return False 

        
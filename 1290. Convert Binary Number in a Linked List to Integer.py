# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        count = 0
        sum = 0
        current = head
        if current.next == None:
            sum = current.val
        else:
            while current != None:
                count += 1
                if count > 1:
                    sum *= 10
                    sum += current.val
                else:
                    sum += current.val
                current = current.next
        result = int(str(sum),2)
        return result
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None
        stackA = []
        stackB = []
        intersect = True
        currentA = headA
        currentB = headB 
        lenA = 0
        lenB = 0
        count = 0
        result = 0
        
        while currentA != None:
            lenA += 1
            stackA.append(id(currentA))
            currentA = currentA.next
        
        while currentB != None:
            lenB += 1
            stackB.append(id(currentB))
            currentB = currentB.next
        
        while intersect:
            if len(stackA) == 0 or len(stackB) == 0:
                break
            valA = stackA.pop()
            valB = stackB.pop()
            if (valA != valB):
                intersect = False
            else:
                count += 1

        if count == 0:
            return None
        
        if lenB <= lenA:
            timeB = lenB - count
            while timeB != 0:
                headB = headB.next
                timeB -= 1
            return headB
            
        else:
            timeA = lenA - count
            while timeA != 0:
                headA = headA.next
                timeA -= 1
            return headA



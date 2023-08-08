# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original is None:
            return None
        if original.val == target.val:
            return cloned

        right =  self.getTargetCopy(original.right,cloned.right,target)
        
        if right:
            return right
        else:
            return self.getTargetCopy(original.left,cloned.left,target)
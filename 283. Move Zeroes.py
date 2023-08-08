class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        stack = []
        # nums.sort()
        for i in nums:
            if nums[i] != 0:
                break
            else:
                stack.append(0)
                del nums[i]
                
        while len(stack) != 0:
            nums.append(stack.pop())

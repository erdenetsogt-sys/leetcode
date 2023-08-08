class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if nums is None:
            return None
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
        
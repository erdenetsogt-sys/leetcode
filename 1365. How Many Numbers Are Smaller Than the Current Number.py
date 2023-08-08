class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        self.count = 0
        self.list = []
        for i in range(len(nums)):
            for k in nums:
                if nums[i] > k:
                    self.count+=1
            self.list.append(self.count)
            self.count = 0
        return self.list
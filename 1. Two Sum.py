class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        count = -1
        for i in nums:
            count += 1
            if i in dict.values():
                val1 = nums.index(target-i)
                val2 = nums.index(i)
                return [val1,count]
            else:
                dict[i] = target - i 
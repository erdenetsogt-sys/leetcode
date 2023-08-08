class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        new_list = []
        j = n
        i = 0
        while i != n:
            new_list.append(nums[i])
            new_list.append(nums[j])
            i +=1
            j +=1
        return new_list
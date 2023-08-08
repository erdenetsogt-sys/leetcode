class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XORを使用して2回現れる要素はキャンセルされる
        # 最終的には、一度しか現れなかった要素の値が残る
        res = 0
        for num in nums:
            res ^= num
        return res

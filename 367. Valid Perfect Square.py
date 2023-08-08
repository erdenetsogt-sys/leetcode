class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 0
        if num == 0:
            return True
        while i <= num:
            if i*i >= num:
                break
            i+=1
        return i*i ==num
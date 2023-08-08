class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        i = 1
        while i < x:
            next = i+1
            if i*i <=x & x < next*next:
                break
            i+=1
        return i
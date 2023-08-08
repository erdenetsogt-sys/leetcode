class Solution:
    def isPalindrome(self, x: int) -> bool:
        result = 0
        count = 0
        if x < 0:
            return False
        for i in str(x):
            print(i)
            result += int(i)*(10**count)
            count += 1
        return result == x
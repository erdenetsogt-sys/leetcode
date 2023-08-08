class Solution:
    def sumOfMultiples(self, n: int) -> int:
        if n < 1:
            return 0

        if n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
            return self.sumOfMultiples(n-1) + n
        else:
            return self.sumOfMultiples(n-1)
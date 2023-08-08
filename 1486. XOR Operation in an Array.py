class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        self.sum = 0
        for i in range(n):
            self.sum = (start + i*2) ^ self.sum
        return self.sum
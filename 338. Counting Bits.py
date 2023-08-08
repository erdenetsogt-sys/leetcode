class Solution:
    def countBits(self, n: int) -> List[int]:
        self.sum = 0
        self.list = []
        for i in range(n + 1):
            for j in bin(i)[2:]:
                if j == "1":
                    self.sum += 1
            self.list.append(self.sum)
            self.sum = 0
        return self.list
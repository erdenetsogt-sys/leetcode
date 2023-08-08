class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        self.count = 0
        self.even = 0
        self.odd = 0
        self.bit = bin(n)[2:][::-1]
        for i in self.bit:
            if i == "1":
                if self.count % 2 == 0:
                    self.even += 1
                else:
                    self.odd += 1
            self.count += 1
        
        return [self.even,self.odd]
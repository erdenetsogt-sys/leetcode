class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = 0
        number = 0
        while len(digits) != 0:
            number += digits.pop() * 10**index
            index += 1
        number += 1
        for i in str(number):
            digits.append(int(i))
        return digits
class Solution:
    def numberOfSteps(self, num: int,step = 0) -> int:
        if num == 0:
            return step

        step += 1

        if num %2 == 0:
            return self.numberOfSteps(num /2,step)
        else:
            return self.numberOfSteps(num - 1,step)
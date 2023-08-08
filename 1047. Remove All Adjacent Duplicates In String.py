class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        str = ""

        for i in s:
            if i not in stack:
                stack.append(i)
            else:
                if i == stack[-1]:
                    stack.pop()
                else:
                    stack.append(i)

        while len(stack) != 0:
            str = stack.pop() + str
        return str
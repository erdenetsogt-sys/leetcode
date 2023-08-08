class Solution:
    def isValid(self, s: str) -> bool:
        p1,p2,p3 = 0,0,0
        for i in s:
            if i == "(":
                p1 += 1
            if i == "[":
                p2 += 1
            if i == "{":
                p3 += 1 
            if i == ")":
                p1 -= 1
            if i == "]":
                p2 -= 1 
            if i == "}":
                p3 -= 1 

        return p1 == 0 and p2 == 0 and p3 == 0
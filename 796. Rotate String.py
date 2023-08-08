
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s == goal:
            return True
        t = s
        for i in range(len(s)-1):
            s = s[1:] + s[0]
            t = t[-1] + t[:-1]

            if s == goal or t == goal:
                return True
        
        return False
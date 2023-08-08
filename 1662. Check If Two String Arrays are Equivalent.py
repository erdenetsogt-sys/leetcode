class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        res1,res2 = "",""

        for i in word1:
            for j in i:
                res1 += j

        for i in word2:
            for j in i:
                res2 += j

        return res1 == res2
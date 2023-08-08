class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = len(sentences[0].split())
        for i in range(1,len(sentences)):
            if ans < len(sentences[i].split()):
                ans = len(sentences[i].split())
            # ans = max(len(sentences[i].split()),len(sentences[i-1].split()))
        return ans
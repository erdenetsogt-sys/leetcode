class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        regular_expression = r'[^\w\s]'
        new_string = re.sub(regular_expression, '', paragraph)
        paragraph = paragraph.split()
        
        dict = {}
        for i in paragraph:
            if i not in banned:
                if i not in dict:
                    dict[i] = 0
                else:
                    dict[i] += 1
        return max(dict.items())[0]
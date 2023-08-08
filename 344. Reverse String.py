class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Reverses a string in-place by modifying the input array

        Args:
            s: a list of characters representing the string to be reversed

        Returns:
            None
        """
        left, right = 0, len(s) - 1  
        while left < right:
            s[left], s[right] = s[right], s[left]  
            left += 1  
            right -= 1  
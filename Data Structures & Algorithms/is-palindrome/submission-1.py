class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Using filter() with str.isalnum()
        # s = ''.join(filter(str.isalnum, s)).lower()
        
        # Using List Comprehension with str.isalnum()
        s = ''.join(ch.lower() for ch in s if ch.isalnum())
        
        return s == s[::-1]
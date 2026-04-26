class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # create set of all unique char
        charSet = set(s)
        res = 0
        
        # iterate through each unique char
        for char in charSet:
            # initialize count and left pointer
            count = l = 0

            # iterate through entire string
            for r in range(len(s)):
                # if right pointer is equal to char, increment count
                if s[r] == char:
                    count += 1
                
                # if replacements exceed k, increment left pointer
                while (r - l + 1) - count > k:
                    if s[l] == char:
                        count -= 1
                    l += 1
                res = max(res, r - l + 1)
        return res

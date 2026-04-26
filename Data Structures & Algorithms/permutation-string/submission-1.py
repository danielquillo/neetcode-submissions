from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = Counter(s1)
        n = len(s1)
        m = len(s2)

        for i in range(m - n + 1):
            freq2 = Counter(s2[i:n +i])
            if freq1 == freq2:
                return True
        return False
        
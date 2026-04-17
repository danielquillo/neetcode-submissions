class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        res = []
        for i in range(k):
            key = max(freq, key = freq.get)
            res.append(key)
            freq.pop(key)
        return res
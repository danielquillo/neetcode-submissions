class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create set of nums
        unique = set(nums)
        
        # iterate nums
        curr_count, count = 0, 0
        for num in nums:
            curr = num
            # check if curr is start of a sequence
            if curr - 1 not in unique:
                # check if next num in sequence is in nums
                while curr + 1 in unique:
                    curr_count += 1
                    curr += 1
                count = max(count, curr_count + 1)
            curr_count = 0

        return count
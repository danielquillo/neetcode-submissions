class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # prefix
        prefix = [1] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = nums[i - 1] * prefix[i - 1]

        # suffix
        suffix = [1] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = nums[i] * suffix[i + 1]

        res = []    
        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i + 1])
        return res


        
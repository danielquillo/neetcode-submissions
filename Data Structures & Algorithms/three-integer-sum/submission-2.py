class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        seen = set()
        ans = []

        for i in range(n):
            target = -nums[i]
            l, r = i + 1, n - 1

            while l < r:
                if nums[l] + nums[r] == target:
                    if (nums[i], nums[l], nums[r]) not in seen:
                        ans.append([nums[i], nums[l], nums[r]])
                        seen.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
        return ans

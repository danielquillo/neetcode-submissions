class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        # binary search
        for i in range(n):
            l, r = i + 1, n - 1

            # nums[i] + nums[mid] = target => nums[mid] = target - nums[i]
            targ = target - numbers[i]

            while l <= r:
                mid = l + (r - l) // 2
                if numbers[mid] == targ:
                    return [min(i, mid) + 1, max(i, mid) + 1]
                elif numbers[mid] < targ:
                    l = mid + 1
                else:
                    r = mid - 1
                     
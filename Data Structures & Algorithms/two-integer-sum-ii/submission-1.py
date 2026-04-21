class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # binary search solution
        # n = len(numbers)
        # for i in range(n):
        #     l, r = i + 1, n - 1

        #     # nums[i] + nums[mid] = target => nums[mid] = target - nums[i]
        #     comp = target - numbers[i]

        #     while l <= r:
        #         mid = l + (r - l) // 2
        #         if numbers[mid] == comp:
        #             return [min(i, mid) + 1, max(i, mid) + 1]
        #         elif numbers[mid] < comp:
        #             l = mid + 1
        #         else:
        #             r = mid - 1

        # hash map solution
        seen = {}

        for i in range(len(numbers)):
            comp = target - numbers[i]

            if comp in seen:
                return [seen[comp] + 1, i + 1]
            else:
                seen[numbers[i]] = i

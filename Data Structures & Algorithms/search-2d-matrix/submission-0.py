class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # initial search of rows
        target_row = -1
        for i in range(len(matrix)):
            first, last = matrix[i][0], matrix[i][-1]
            if first <= target <= last:
                target_row = i
        
        if target_row == -1:
            return False
        
        l, r = 0,  len(matrix[0]) - 1
        while l <= r:
            mid = l + ((r - l) // 2)

            if matrix[target_row][mid] == target:
                return True
            elif matrix[target_row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
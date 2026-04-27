import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        first_cols = list(map(lambda x: x[0], matrix))
        row = bisect.bisect_left(first_cols, target)
        t, b = 0, len(matrix[0])
        while t < b:
            mid = (t + b) // 2
            if target < matrix[0][mid]:
                t = mid + 1
            elif target > matrix[0][mid]:
                b = mid - 1
            else:
                return True
        if row == len(first_cols) or row > 0 and matrix[row][0] > target:
            row -= 1
        col = bisect.bisect_left(matrix[row], target)
        return col < len(matrix[0]) and matrix[row][col] == target
            
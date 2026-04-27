import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        first_cols = list(map(lambda x: x[0], matrix))
        row = bisect.bisect_left(first_cols, target)
        if row == len(first_cols) or row > 0 and matrix[row][0] > target:
            row -= 1
        col = bisect.bisect_left(matrix[row], target)
        return col < len(matrix[0]) and matrix[row][col] == target
            
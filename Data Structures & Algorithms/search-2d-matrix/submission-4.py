class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        i = 0
        j = rows*cols
        while i<=j:
            mid = (i+j)//2
            midRow = mid//cols
            midcol = mid%cols
            if matrix[midRow][midcol] == target:
                return True
            if matrix[midRow][midcol] > target:
                j = mid - 1
            else:
                i = mid + 1
        return False
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols = len(matrix),len(matrix[0])
        low = 0
        high = rows*cols - 1 
        while low <= high:
            mid = (high+low)//2
            if matrix[mid//cols][mid%cols] == target:
                return True
            if matrix[mid//cols][mid%cols] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False 
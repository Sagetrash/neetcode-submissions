class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lowrow = 0
        highrow = len(matrix)-1
        while lowrow <= highrow:
            currow = (lowrow+highrow)//2
            i = 0
            j = len(matrix[currow])-1
            while i<=j:
                mid = (i+j)//2
                if matrix[currow][mid] == target:
                    return True
                if matrix[currow][mid] > target:
                    i = mid+1
                else:
                    j = mid-1
            if matrix[currow][0] > target:
                highrow = currow - 1
            else:
                lowrow = currow + 1
        return False
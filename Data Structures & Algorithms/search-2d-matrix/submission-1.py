class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        COL = len(matrix[0])
        ROW = len(matrix)
        i = COL-1
        j = 0
        while i >= 0 and j< ROW:
            if target == matrix[j][i]:
                return True
            elif matrix[j][i] < target:
                j += 1
            else:
                i -= 1 
        
        return False
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])

        l, r = 0, R*C - 1

        while l <= r:
            mean = (l + r)//2
            row = mean//C
            col = mean%C

            if target > matrix[row][col]:
                l = mean + 1
            elif target < matrix[row][col]:
                r = mean - 1
            elif target == matrix[row][col]:
                return True
            
        return False
        
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if target >= i[0] and target <= i[-1]:
                l, r = 0, len(i) - 1

                while l <= r:
                    mean = (l + r)//2
                    if target > i[mean]:
                        l = mean + 1
                    elif target < i[mean]:
                        r = mean - 1
                    elif target == i[mean]:
                        return True
                
        return False

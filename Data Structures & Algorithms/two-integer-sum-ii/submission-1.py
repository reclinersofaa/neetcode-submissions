class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            csum = numbers[l] + numbers[r]

            if csum > target: #csum is too big, reduce by moving to lesser num
                r -= 1
            elif csum < target: #csum is too small, increase by moving to larger num
                l += 1
            else:
                return [l+1, r+1]
        return []
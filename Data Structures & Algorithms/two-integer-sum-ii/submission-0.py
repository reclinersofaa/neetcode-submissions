class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = {}
            
        for i,n in enumerate(numbers):
            diff = target - n
            if diff in res:
                print(diff,i,n)
                return [res[diff] + 1,i + 1]
            res[n] = i 